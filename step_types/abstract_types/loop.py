from step_types.helpers import get_entity_type

from step_types.edge_loop import EdgeLoop
from step_types.vertex_loop import VertexLoop


def parse(conn, id: int):
    type = get_entity_type(conn, id)
    # print('parsing loop', type)
    if type == 'EDGE_LOOP':
        return EdgeLoop(conn, id)
    elif type == 'VERTEX_LOOP':
        return VertexLoop(conn, id)
    # TODO: POLY_LOOP
    raise Exception(f'Cannot find context with type {type}')

