from typing import List, Union, Tuple
import re

def split_arguments(arg_string: str) -> List[str]:
    """Splits arguments while handling parentheses (nested lists)."""
    args = []
    depth = 0
    escaped = None 
    current = ''
    for char in arg_string:
        if escaped is None and char == "'":
            escaped = char
            current += char
        elif escaped == char:
            escaped = None
            current += char
        elif escaped is None and char == ',' and depth == 0:
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

def classify_arg(arg: str) -> Tuple[str, Union[str, None]]:
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

