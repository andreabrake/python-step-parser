from step_types.helpers import get_arguments, clean_display_doublelist
from step_types.cartesian_point import CartesianPoint

class BSplineSurfaceWithKnots():
    def __init__(self, conn, key: int):
        self.key = key
        self.__get_arguments(conn)
        pass

    def __str__(self):
        return f'''B_SPLINE_SURFACE_WITH_KNOTS (
    key          = {self.key}
    name         = {self.name}
    udegree      = {self.udegree}
    vdegree      = {self.vdegree}
    control_pts  = {clean_display_doublelist(self.control_points_list)}
    surface_form = {self.surface_form}
    uclosed      = {self.uclosed}
    vclosed      = {self.vclosed}
    self_insect  = {self.self_intersect}
    umults       = {self.umultiplicities}
    vmults       = {self.vmultiplicities}
    uknots       = {self.uknots}
    vknots       = {self.vknots}
    knot_spec    = {self.knot_spec}
)
'''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        self.name = args[0]
        self.udegree = args[1]
        self.vdegree = args[2]
        self.control_points_list = [[CartesianPoint(conn, p) for p in ps] for ps in args[3]]
        self.surface_form = args[4]
        self.uclosed = args[5]
        self.vclosed = args[6]
        self.self_intersect = args[7]
        self.umultiplicities = args[8]
        self.vmultiplicities = args[9]
        self.uknots = args[10]
        self.vknots = args[11]
        self.knot_spec = args[12]