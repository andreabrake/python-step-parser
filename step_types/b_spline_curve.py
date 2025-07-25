from .helpers import get_complex_or_base_arguments, clean_display_list
from .bounded_curve import BoundedCurve
from .cartesian_point import CartesianPoint

class BSPlineCurve(BoundedCurve):
    type_name = 'B_SPLINE_CURVE'

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
    degree       = {self.degree}
    control_pts  = {clean_display_list(self.control_points_list)}
    curve_form   = {self.curve_form}
    closed_curve = {self.closed_curve}
    self_insect  = {self.self_intersect}'''
    
    def __get_arguments(self, conn):
        args = get_complex_or_base_arguments(conn,
                                             self.key,
                                             ['REPRESENTATION_ITEM',
                                              'GEOMETRIC_REPRESENTATION_ITEM',
                                              'CURVE',
                                              'BOUNDED_CURVE',
                                              'B_SPLINE_CURVE'])
        
        self.degree = args[1]
        self.control_points_list = [CartesianPoint(conn, p) for p in args[2]]
        self.curve_form = args[3]
        self.closed_curve = args[4]
        self.self_intersect = args[5]

    def get_geometry(self):
        return super().get_geometry() | {
            'type': self.type_name,
            'deg': self.degree,
            'pts': [p.get_geometry() for p in self.control_points_list],
            'form': self.curve_form,
            'is_closed': self.closed_curve,
            'is_self_insersect': self.self_intersect
        }