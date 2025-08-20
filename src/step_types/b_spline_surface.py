from .helpers import get_arguments, clean_display_doublelist
from .bounded_surface import BoundedSurface
from .cartesian_point import CartesianPoint

class BSPlineSurface(BoundedSurface):
    type_name = 'B_SPLINE_SURFACE'

    def __init__(self, conn, key: int):
        super().__init__(conn, key)
        self.__get_arguments(conn)

    def __str__(self):
        return f'''{self.type_name} (
{self._str_args()}
)
'''

    def _str_args(self):
        return f'''{super()._str_args()}
    udegree      = {self.udegree}
    vdegree      = {self.vdegree}
    control_pts  = {clean_display_doublelist(self.control_points_list)}
    surface_form = {self.surface_form}
    uclosed      = {self.uclosed}
    vclosed      = {self.vclosed}
    self_insect  = {self.self_intersect}'''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)

        self.udegree = args[1]
        self.vdegree = args[2]
        self.control_points_list = [[CartesianPoint(conn, p) for p in ps] for ps in args[3]]
        self.surface_form = args[4]
        self.uclosed = args[5]
        self.vclosed = args[6]
        self.self_intersect = args[7]