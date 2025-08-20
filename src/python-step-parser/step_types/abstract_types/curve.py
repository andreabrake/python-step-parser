from ..helpers import get_entity_type, get_complex_items

from ..line import Line
from ..circle import Circle
from ..ellipse import Ellipse
from ..b_spline_curve_with_knots import BSplineCurveWithKnots

from ..rational_b_spline_curve import RationalBSplineCurve

def parse_curve(parser, id: int):
    type = get_entity_type(parser, id)
    # print('parsing curve', type)
    if type == 'CIRCLE':
        return Circle(parser, id)
    elif type == 'ELLIPSE':
        return Ellipse(parser, id)
    elif type == 'B_SPLINE_CURVE_WITH_KNOTS':
        return BSplineCurveWithKnots(parser, id)
    elif type == 'LINE':
        return Line(parser, id)
    elif type == 'COMPLEX':
        complex_items = get_complex_items(parser, id)
        complex_item_types = [i.type for i in complex_items]
        if 'RATIONAL_B_SPLINE_CURVE' in complex_item_types:
            return RationalBSplineCurve(parser, id)
        raise Exception(f'Cannot find context with type {type} [{','.join(complex_item_types)}]')
    raise Exception(f'Cannot find context with type {type}')

