from step_types.helpers import get_entity_type, get_complex_items
from step_types.next_assembly_usage_occurance import NextAssemblyUsageOccurrence

def parse(conn, id: int):
    type = get_entity_type(conn, id)
    if type == 'NEXT_ASSEMBLY_USAGE_OCCURRENCE':
        return NextAssemblyUsageOccurrence(conn, id)
    raise Exception(f'Could not parse entity type {type}(id)')