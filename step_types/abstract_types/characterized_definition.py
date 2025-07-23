from step_types.helpers import get_entity_type, get_complex_items
from step_types.next_assembly_usage_occurance import NextAssemblyUsageOccurrence
from step_types.product_definition_formation_with_source import ProductDefinitionFormationWithSource

def parse(conn, id: int):
    type = get_entity_type(conn, id)
    if type == 'NEXT_ASSEMBLY_USAGE_OCCURRENCE':
        return NextAssemblyUsageOccurrence(conn, id)
    if type == 'PRODUCT_DEFINITION_FORMATION_WITH_SPECIFIED_SOURCE':
        return ProductDefinitionFormationWithSource(conn, id)
    raise Exception(f'Could not parse entity type {type}(id)')