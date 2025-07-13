from step_types.helpers import get_entity_type

from step_types.axis2_placement3d import Axis2Placement3d
from step_types.advanced_face import AdvancedFace

def parse(conn, id: int):
    type = get_entity_type(conn, id)
    # print('parsing relationship item', type, id)
    if type == 'AXIS2_PLACEMENT_3D':
        return Axis2Placement3d(conn, id)
    raise Exception(f'Cannot fine relationship_item with type {type}')
