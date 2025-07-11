from parsers.helpers import get_entity_type

from parsers.manifold_solid_brep import ManifoldSolidBrep
from parsers.advanced_face import AdvancedFace

def parse_item(conn, id: int):
    type = get_entity_type(conn, id)
    print('parsing item', type, id)
    if type == 'MANIFOLD_SOLID_BREP':
        return ManifoldSolidBrep(conn, id)
    else:
        return AdvancedFace(conn, id)
