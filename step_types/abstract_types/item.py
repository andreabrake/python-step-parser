from ..helpers import get_entity_type

from ..manifold_solid_brep import ManifoldSolidBrep
from ..advanced_face import AdvancedFace

def parse_item(conn, id: int):
    type = get_entity_type(conn, id)
    # print('parsing item', type, id)
    if type == 'MANIFOLD_SOLID_BREP':
        return ManifoldSolidBrep(conn, id)
    elif type == 'ADVANCED_FACE':
        return AdvancedFace(conn, id)
    raise Exception(f'Cannot find item with type {type}')

