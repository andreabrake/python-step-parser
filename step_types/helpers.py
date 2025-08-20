import sqlite3
from typing import List
import itertools

class ChildTypeRegister():
    def __init__(self, name, base_registers=None):
        self.name = name
        self.base_registers = base_registers
        self.child_type_register = {}

    def try_parse(self, conn, id: int):
        type = get_entity_type(conn, id)
        if type == 'COMPLEX':
            complex_items = get_complex_items(conn, id)
            complex_item_types = [i.type for i in complex_items]
            for resolved_type in complex_item_types:
                if resolved_type in self.child_type_register:
                    # print('resolving', id, 'as', resolved_type)
                    return self.child_type_register[resolved_type](conn, id)
            return None
        if type in self.child_type_register:
            return self.child_type_register[type](conn, id)
        return None

    def parse(self, conn, id: int):
        type = get_entity_type(conn, id)
        if type == 'COMPLEX':
            complex_items = get_complex_items(conn, id)
            complex_item_types = [i.type for i in complex_items]
            for resolved_type in complex_item_types:
                if resolved_type in self.child_type_register:
                    # print('resolving', id, 'as', resolved_type)
                    return self.child_type_register[resolved_type](conn, id)
            raise Exception(f'Cannot find context with type {type} [{','.join(complex_item_types)}]')
        if type in self.child_type_register:
            return self.child_type_register[type](conn, id)
        raise Exception(f'Cannot find {self.name} with type {type}')
    
    def register(self, type_name: str, type_val):
        self.child_type_register[type_name] = type_val
        if self.base_registers is not None:
            if isinstance(self.base_registers, list):
                for r in self.base_registers:
                    r.register(type_name, type_val)
            else:
                self.base_registers.register(type_name, type_val)
            
class ComplexItemDTO:
    type: str
    arg_offset: int
    n_args: int

    def __init__(self, type: str, arg_offset: int, n_args: int):
        self.type = type
        self.arg_offset = arg_offset
        self.n_args = n_args

entity_type_cache = {}
complex_item_cache = {}
arg_cache = {}
list_text_cache = {}
parent_ref_cache = {}

def parse_arg_value(value_type: str, value_text: str):
    if value_type == 'list':
        return [int(v[1:]) if v[0] == '#' else v
                for v
                in [v.strip()
                    for v
                    in value_text[1:len(value_text)-1].split(',')]]
    if value_type == 'reference':
        return int(value_text)
    if value_type == 'number':
        return float(value_text)
    return value_text

def get_list_text(conn: sqlite3.Connection, argument_id: int, depth:int=0):
    if argument_id in list_text_cache:
        return list_text_cache[argument_id]
    cursor = conn.cursor()
    cursor.execute(f"""
                   SELECT value_type, value_text
                   FROM step_list_items
                   WHERE argument_id={argument_id}
                   ORDER BY item_index;""")
    val = [
        parse_arg_value(row[0].strip(), row[1].strip() if row[1] is not None else None)
        for row
        in cursor.fetchall()
    ]
    list_text_cache[argument_id] = val
    return val

def parse_arg_value_with_traversal(conn: sqlite3.Connection, argument_id: int, value_type: str, value_text: str):
    if value_type == 'list':
        return get_list_text(conn, argument_id)
    return parse_arg_value(value_type, value_text)

def get_arguments(conn: sqlite3.Connection, entity_id: int):
    if entity_id in arg_cache:
        return arg_cache[entity_id]
    print(f'cache miss {entity_id} ({type(entity_id)})')

    cursor = conn.cursor()
    cursor.execute(f"""
                   SELECT id, value_type, value_text
                   FROM step_arguments
                   WHERE entity_id={entity_id}
                   ORDER BY arg_index;""")
    args = [
        parse_arg_value(conn, row[0], row[1].strip(), row[2].strip())
        for row
        in cursor.fetchall()
    ]
    arg_cache[entity_id] = args
    return args

def get_complex_or_base_arguments(conn: sqlite3.Connection, entity_id: int, complex_types: List[str]):
    args = get_arguments(conn, entity_id)
    complex_items = get_complex_items(conn, entity_id)
    if len(complex_items) > 0:
        return get_all_complex_args(args,
                                    complex_items,
                                    complex_types)
    return args

def get_complex_items(conn: sqlite3.Connection, entity_id: int) -> List[ComplexItemDTO]:
    if entity_id in complex_item_cache:
        return complex_item_cache[entity_id]
    
    cursor = conn.cursor()
    cursor.execute(f"""
                   SELECT entity_id, item_index, type, step_arguments_offset, n_args
                   FROM step_complex_items
                   WHERE entity_id={entity_id}
                   ORDER BY item_index;""")
    items = [
        ComplexItemDTO(row[2], int(row[3]), int(row[4]))
        for row
        in cursor.fetchall()
    ]

    complex_item_cache[entity_id] = items
    return items

def get_complex_args(args: List[str], types: List[ComplexItemDTO], type_name: str) -> List[str]:
    ci = next((t for t in types if t.type == type_name), None)
    if ci is None:
        return []
    return args[ci.arg_offset:(ci.arg_offset + ci.n_args)]

def get_all_complex_args(args: List[str], types: List[ComplexItemDTO], type_names: List[str]) -> List[str]:
    return list(itertools.chain.from_iterable([
        get_complex_args(args, types, t)
        for t in type_names
    ]))

def get_entity_list(conn: sqlite3.Connection, type: str) -> List[int]:
    cursor = conn.cursor()
    cursor.execute(f"SELECT Id FROM step_entities WHERE type = '{type}';")
    return [int(row[0]) for row in cursor.fetchall()]

def get_entity_type(conn: sqlite3.Connection, id: int) -> str:
    if id in entity_type_cache:
        return entity_type_cache[id]
    cursor = conn.cursor()
    cursor.execute(f"SELECT type FROM step_entities WHERE Id = '{id}';")
    val = [str(row[0]).upper() for row in cursor.fetchall()][0]
    entity_type_cache[id] = val
    return val

def clean_display(val, padding='    '):
    if val is None:
        return 'n/a'
    return str(val).replace('\n', f'\n{padding}').strip()

def clean_display_doublelist(vals, padding='    '):
    if vals is None:
        return '[]'
    return f'''[
    {padding}{f'\n{padding}'.join([
        clean_display_list(v) for v in vals
    ]).replace('\n', f'\n{padding}').strip()}
{padding}]'''

def clean_display_list(vals, padding='    '):
    if vals is None:
        return '[]'
    return f'''[
    {padding}{f'\n{padding}'.join([
        clean_display(v) for v in vals
    ]).replace('\n', f'\n{padding}').strip()}
{padding}]'''

def get_parents(id: int) -> List[int]:
    return [] if id not in parent_ref_cache else parent_ref_cache[id]

def get_representation_contexts(conn: sqlite3.Connection) -> List[int]:
    cursor = conn.cursor()

    cursor.execute(f"""
                   SELECT id
                   FROM step_entities
                   WHERE type IN ('GEOMETRIC_REPRESENTATION_CONTEXT')
                   ORDER BY id""")
    
    simple_entities = [int(row[0]) for row in cursor.fetchall()]
    
    cursor.execute(f"""
                   SELECT distinct entity_id
                   FROM step_complex_items
                   WHERE type = 'GEOMETRIC_REPRESENTATION_CONTEXT'
                   ORDER BY entity_id""")
    
    complex_entities = [int(row[0]) for row in cursor.fetchall()]
    
    cursor.close()
    
    return simple_entities + complex_entities

def load_all_cache(conn: sqlite3.Connection) -> None:
    print('[*] Loaded data cache')

    cursor = conn.cursor()

    # Load entities
    cursor.execute(f"SELECT Id, type FROM step_entities;")
    i = 0
    for row in cursor.fetchall():
        entity_type_cache[int(row[0])] = str(row[1]).upper()
        i+=1

    print(f'[*] Loaded {i} step_entities into memory cache')
    
    # Load complex items
    cursor.execute(f"""
                   SELECT entity_id, item_index, type, step_arguments_offset, n_args
                   FROM step_complex_items
                   ORDER BY entity_id, item_index;""")
    i = 0
    for row in cursor.fetchall():
        entity_id = int(row[0])
        if entity_id not in complex_item_cache:
            complex_item_cache[entity_id] = []
        complex_item_cache[entity_id].append(ComplexItemDTO(row[2], int(row[3]), int(row[4])))
        i+=1

    print(f'[*] Loaded {i} step_complex_items into memory cache')

    # Load step list items
    cursor.execute(f"""
                   SELECT argument_id, value_type, value_text
                   FROM step_list_items
                   ORDER BY argument_id, item_index;""")
    i = 0
    for row in cursor.fetchall():
        argument_id = int(row[0])
        if argument_id not in list_text_cache:
            list_text_cache[argument_id] = []
        list_text_cache[argument_id].append(parse_arg_value(row[1].strip(), row[2].strip()))
        i+=1

    print(f'[*] Loaded {i} step_list_items into memory cache')

    # Load arguments
    cursor.execute(f"""
                   SELECT entity_id, id, value_type, value_text
                   FROM step_arguments
                   ORDER BY entity_id, arg_index;""")
    i = 0
    for row in cursor.fetchall():
        entity_id = int(row[0])
        if entity_id not in arg_cache:
            arg_cache[entity_id] = []
        value_type = str(row[2]).strip()
        value_text = str(row[3]).strip() if row[3] is not None else None
        arg_cache[entity_id].append(parse_arg_value_with_traversal(None, int(row[1]), value_type, value_text))
        
        if value_type.lower() == 'reference':
            ref_id = int(value_text)
            if ref_id not in parent_ref_cache:
                parent_ref_cache[ref_id] = []
            parent_ref_cache[ref_id].append(entity_id)
        i+=1

    print(f'[*] Loaded {i} step_arguments into memory cache')

    cursor.close()
