from step_types.helpers import get_entity_type

from step_types.axis2_placement3d import Axis2Placement3d
from step_types.advanced_face import AdvancedFace
from step_types.manifold_solid_brep import ManifoldSolidBrep
from step_types.shape_representation import ShapeRepresentation

dynamic_register = {}

def parse(conn, id: int):
    type = get_entity_type(conn, id)
    # print('parsing relationship item', type, id)
    if type == 'AXIS2_PLACEMENT_3D':
        return Axis2Placement3d(conn, id)
    if type == 'MANIFOLD_SOLID_BREP':
        return ManifoldSolidBrep(conn, id)
    if type == 'SHAPE_REPRESENTATION':
        return ShapeRepresentation(conn, id)
    if type in dynamic_register:
        dynamic_register[type](conn, id)
    raise Exception(f'Cannot find relationship_item with type {type}')

def register(type_name: str, type_val):
    dynamic_register[type_name] = type_val