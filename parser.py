import re
import sqlite3
from typing import List, Dict, Union

# --- STEP Parsing Functions ---

def split_arguments(arg_string: str) -> List[str]:
    """Splits arguments while handling parentheses (nested lists)."""
    args = []
    depth = 0
    current = ''
    for char in arg_string:
        if char == ',' and depth == 0:
            args.append(current.strip())
            current = ''
        else:
            if char == '(':
                depth += 1
            elif char == ')':
                depth -= 1
            current += char
    if current:
        args.append(current.strip())
    return args

def classify_arg(arg: str) -> (str, Union[str, None]):
    """Returns (type, value_text) for an argument."""
    arg = arg.strip()
    if not arg or arg == '$':
        return 'null', None
    if arg.startswith("'") and arg.endswith("'"):
        return 'string', arg.strip("'")
    if re.match(r'^#\d+$', arg):
        return 'reference', arg[1:]  # store just the ID number
    if arg.startswith('(') and arg.endswith(')'):
        return 'list', arg  # will be handled separately
    if re.match(r'^-?\d+(\.\d+)?$', arg):
        return 'number', arg
    return 'string', arg.strip("'")  # fallback

def parse_step_file(filepath: str) -> Dict[int, Dict]:
    """Parses STEP and returns entities."""
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    data_match = re.search(r"DATA;(.*?)ENDSEC;", content, re.DOTALL | re.IGNORECASE)
    if not data_match:
        raise ValueError("No DATA section found in STEP file.")

    data = data_match.group(1).strip()
    entities = {}

    lines = data.splitlines()
    n = len(lines)

    for i in range(0, n):
        if i % 1000 == 0:
            print(f'parsed line {i}')
        line = lines[i]
        while ';' not in line:
            line += f' {lines[i + 1]}'
            i += 1
        line = line.strip().rstrip(';')
        if not line.startswith('#'):
            continue
        m = re.match(r"#(\d+)\s*=\s*(\w+)\((.*)\)", line)
        if m:
            entity_id = int(m.group(1))
            entity_type = m.group(2)
            raw_args = m.group(3)
            args = split_arguments(raw_args)
            entities[entity_id] = {
                'type': entity_type,
                'args': args
            }
    return entities

# --- SQLite Setup ---

def init_db(db_file: str):
    conn = sqlite3.connect(db_file)
    c = conn.cursor()

    # Create tables
    c.execute("""
        CREATE TABLE IF NOT EXISTS step_entities (
            id INTEGER PRIMARY KEY,
            type TEXT NOT NULL
        );
    """)
    c.execute("""
        CREATE TABLE IF NOT EXISTS step_arguments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            entity_id INTEGER NOT NULL,
            arg_index INTEGER NOT NULL,
            value_type TEXT NOT NULL,
            value_text TEXT,
            FOREIGN KEY(entity_id) REFERENCES step_entities(id)
        );
    """)
    c.execute("""
        CREATE TABLE IF NOT EXISTS step_list_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            argument_id INTEGER NOT NULL,
            item_index INTEGER NOT NULL,
            value_type TEXT NOT NULL,
            value_text TEXT,
            FOREIGN KEY(argument_id) REFERENCES step_arguments(id)
        );
    """)
    conn.commit()
    return conn

# --- DB Insertion Logic ---

def insert_entity(conn, entity_id: int, entity_type: str):
    cursor = conn.cursor()
    # Insert or replace the entity
    cursor.execute("""
        INSERT INTO step_entities (id, type)
        VALUES (?, ?)
        ON CONFLICT(id) DO UPDATE SET type=excluded.type;
    """, (entity_id, entity_type))

def insert_argument(conn, entity_id: int, index: int, value_type: str, value_text: Union[str, None]) -> int:
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO step_arguments (entity_id, arg_index, value_type, value_text)
        VALUES (?, ?, ?, ?);
    """, (entity_id, index, value_type, value_text))
    return cursor.lastrowid

def insert_list_items(conn, argument_id: int, list_string: str):
    cursor = conn.cursor()
    list_items = split_arguments(list_string[1:-1])  # strip parentheses
    for i, item in enumerate(list_items):
        vtype, vtext = classify_arg(item)
        cursor.execute("""
            INSERT INTO step_list_items (argument_id, item_index, value_type, value_text)
            VALUES (?, ?, ?, ?);
        """, (argument_id, i, vtype, vtext))

def save_entities_to_db(conn, entities: Dict[int, Dict]):
    for entity_id, data in entities.items():
        entity_type = data['type']
        insert_entity(conn, entity_id, entity_type)

        for i, raw_arg in enumerate(data['args']):
            value_type, value_text = classify_arg(raw_arg)
            arg_id = insert_argument(conn, entity_id, i, value_type, value_text)
            if value_type == 'list':
                insert_list_items(conn, arg_id, value_text)

    conn.commit()

# --- Main Execution ---

def parse_and_store_step(step_file: str, db_file: str):
    entities = parse_step_file(step_file)
    print('parsed step file')
    conn = init_db(db_file)
    print('db initialized')
    save_entities_to_db(conn, entities)
    conn.close()
    print(f"STEP file parsed and saved to '{db_file}'.")

# --- Run it ---
if __name__ == "__main__":
    project_name = "<FILE_NAME>"
    parse_and_store_step(f'{project_name}.stp', f'{project_name}.db')  # Change to your STEP file
