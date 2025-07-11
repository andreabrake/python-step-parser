from step_types.helpers import get_entity_type

from step_types.manifold_solid_brep import ManifoldSolidBrep
from step_types.advanced_face import AdvancedFace

def parse_item(conn, id: int):
    type = get_entity_type(conn, id)
    print('parsing item', type, id)
    if type == 'MANIFOLD_SOLID_BREP':
        return ManifoldSolidBrep(conn, id)
    else:
        return AdvancedFace(conn, id)
