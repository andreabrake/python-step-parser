from ..helpers import get_entity_type

from ..edge_loop import EdgeLoop
from ..vertex_loop import VertexLoop
from ..poly_loop import PolyLoop
from ..loop import Loop


def parse(parser, id: int) -> Loop:
    type = get_entity_type(parser, id)
    # print('parsing loop', type)
    if type == 'EDGE_LOOP':
        return EdgeLoop(parser, id)
    elif type == 'VERTEX_LOOP':
        return VertexLoop(parser, id)
    elif type == 'POLY_LOOP':
        return PolyLoop(parser, id)
    raise Exception(f'Cannot find context with type {type}')

