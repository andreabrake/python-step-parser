from step_types.helpers import get_entity_type, get_complex_items
from step_types.geometric_representation_context import GeometricRepresentationContext

def parse(conn, id: int):
    type = get_entity_type(conn, id)
    # print('parsing relationship item', type, id)
    if type == 'COMPLEX':
        complex_items = get_complex_items(conn, id)
        complex_item_types = [i.type for i in complex_items]
        if 'GEOMETRIC_REPRESENTATION_CONTEXT' in complex_item_types:
            return GeometricRepresentationContext(conn, id)
        raise Exception(f'Cannot find context with type {type} [{','.join(complex_item_types)}]')
    raise Exception(f'Cannot find context with type {type}')
