from step_types.helpers import get_entity_type, get_complex_items

from step_types.solid_angle_unit import SolidAngleUnit
from step_types.plane_angle_unit import PlaneAngleUnit
from step_types.length_unit import LengthUnit
from step_types.uncertainty_measure_with_unit import UncertaintyMeasureWithUnit

def parse(conn, id: int):
    type = get_entity_type(conn, id)
    # print('parsing unit', type)
    if type == 'SOLID_ANGLE_UNIT':
        return SolidAngleUnit(conn, id)
    elif type == 'PLANE_ANGLE_UNIT':
        return PlaneAngleUnit(conn, id)
    elif type == 'LENGTH_UNIT':
        return LengthUnit(conn, id)
    elif type == 'UNCERTAINTY_MEASURE_WITH_UNIT':
        return UncertaintyMeasureWithUnit(conn, id)
    elif type == 'COMPLEX':
        complex_items = get_complex_items(conn, id)
        complex_item_types = [i.type for i in complex_items]
        if 'SOLID_ANGLE_UNIT' in complex_item_types:
            return SolidAngleUnit(conn, id)
        elif 'PLANE_ANGLE_UNIT' in complex_item_types:
            return PlaneAngleUnit(conn, id)
        elif 'LENGTH_UNIT' in complex_item_types:
            return LengthUnit(conn, id)
        elif 'UNCERTAINTY_MEASURE_WITH_UNIT' in complex_item_types:
            return UncertaintyMeasureWithUnit(conn, id)
        raise Exception(f'Cannot find context with type {type} [{','.join(complex_item_types)}]')
    raise Exception(f'Cannot find context with type {type}')
