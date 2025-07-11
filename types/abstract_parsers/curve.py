from parsers.helpers import get_entity_type

from parsers.line import Line
from parsers.circle import Circle
from parsers.ellipse import Ellipse
from parsers.b_spline_curve_with_knots import BSplineCurveWithKnots

def parse_curve(conn, id: int):
    type = get_entity_type(conn, id)
    print('parsing curve', type)
    if type == 'CIRCLE':
        return Circle(conn, id)
    elif type == 'ELLIPSE':
        return Ellipse(conn, id)
    elif type == 'B_SPLINE_CURVE_WITH_KNOTS':
        return BSplineCurveWithKnots(conn, id)
    else:
        return Line(conn, id)
