from ..helpers import get_entity_type, get_complex_items

from ..solid_angle_unit import SolidAngleUnit
from ..plane_angle_unit import PlaneAngleUnit
from ..length_unit import LengthUnit
from ..uncertainty_measure_with_unit import UncertaintyMeasureWithUnit

def parse(parser, id: int):
    type = get_entity_type(parser, id)
    # print('parsing unit', type)
    if type == 'SOLID_ANGLE_UNIT':
        return SolidAngleUnit(parser, id)
    elif type == 'PLANE_ANGLE_UNIT':
        return PlaneAngleUnit(parser, id)
    elif type == 'LENGTH_UNIT':
        return LengthUnit(parser, id)
    elif type == 'UNCERTAINTY_MEASURE_WITH_UNIT':
        return UncertaintyMeasureWithUnit(parser, id)
    elif type == 'COMPLEX':
        complex_items = get_complex_items(parser, id)
        complex_item_types = [i.type for i in complex_items]
        if 'SOLID_ANGLE_UNIT' in complex_item_types:
            return SolidAngleUnit(parser, id)
        elif 'PLANE_ANGLE_UNIT' in complex_item_types:
            return PlaneAngleUnit(parser, id)
        elif 'LENGTH_UNIT' in complex_item_types:
            return LengthUnit(parser, id)
        elif 'UNCERTAINTY_MEASURE_WITH_UNIT' in complex_item_types:
            return UncertaintyMeasureWithUnit(parser, id)
        raise Exception(f'Cannot find context with type {type} [{','.join(complex_item_types)}]')
    raise Exception(f'Cannot find context with type {type}')
