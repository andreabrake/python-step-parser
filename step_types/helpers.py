import sqlite3
from typing import List

entity_type_cache = {}
arg_cache = {}

def manual_list_parse(list_vals):
    return [v[1:] for v in list_vals[1:len(list_vals)-1].split(',')]

def get_list_text(conn: sqlite3.Connection, argument_id: int):
    cursor = conn.cursor()
    cursor.execute(f"SELECT value_type, value_text FROM step_list_items WHERE argument_id={argument_id} ORDER BY item_index;")
    return [
        manual_list_parse(row[1]) if row[0].upper() == 'LIST' else row[1]
        for row
        in cursor.fetchall()
    ]

def parse_arg_value(conn: sqlite3.Connection, argument_id: int, value_type: str, value_text: str):
    if value_type == 'list':
        return get_list_text(conn, argument_id)
    # TODO: parse other data types, e.g. numerics
    return value_text

def get_arguments(conn: sqlite3.Connection, entity_id: int):
    if entity_id in arg_cache:
        return arg_cache[entity_id]
    cursor = conn.cursor()
    cursor.execute(f"SELECT id, value_type, value_text FROM step_arguments WHERE entity_id={entity_id} ORDER BY arg_index;")
    args = [
        parse_arg_value(conn, row[0], row[1], row[2])
        for row
        in cursor.fetchall()
    ]
    arg_cache[entity_id] = args
    return args

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



def load_all_cache(conn: sqlite3.Connection) -> None:
    cursor = conn.cursor()
    cursor.execute(f"SELECT Id, type FROM step_entities;")
    for row in cursor.fetchall():
        entity_type_cache[int(row[0])] = str(row[1]).upper()