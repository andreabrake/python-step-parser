from ..helpers import get_entity_type

from ..edge_loop import EdgeLoop
from ..vertex_loop import VertexLoop
from ..poly_loop import PolyLoop
from ..loop import Loop


def parse(conn, id: int) -> Loop:
    type = get_entity_type(conn, id)
    # print('parsing loop', type)
    if type == 'EDGE_LOOP':
        return EdgeLoop(conn, id)
    elif type == 'VERTEX_LOOP':
        return VertexLoop(conn, id)
    elif type == 'POLY_LOOP':
        return PolyLoop(conn, id)
    raise Exception(f'Cannot find context with type {type}')

