from parsers.helpers import get_arguments, clean_display, clean_display_list
from parsers.cartesian_point import CartesianPoint
from parsers.vertex_point import VertexPoint

class BSplineCurveWithKnots():
    def __init__(self, conn, key: int):
        self.key = key
        self.__get_arguments(conn)
        pass

    def __str__(self):
        return f'''B_SPLINE_CURVE_WITH_KNOTS (
    key          = {self.key}
    name         = {self.name}
    degree       = {self.degree}
    control_pts  = {clean_display_list(self.control_points_list)}
    curve_form   = {self.curve_form}
    closed_curve = {self.closed_curve}
    self_insect  = {self.self_intersect}
    knot_mult    = {self.knot_multiplicities}
    knots        = {self.knots}
    knot_spec    = {self.knot_spec}
)
'''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        self.name = args[0]
        self.degree = args[1]
        self.control_points_list = [CartesianPoint(conn, p) for p in args[2]]
        self.curve_form = args[3]
        self.closed_curve = args[4]
        self.self_intersect = args[5]
        self.knot_multiplicities = args[6]
        self.knots = args[7]
        self.knot_spec = args[8]