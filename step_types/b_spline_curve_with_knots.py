from .helpers import get_complex_or_base_arguments, clean_display_list
from .b_spline_curve import BSPlineCurve

class BSplineCurveWithKnots(BSPlineCurve):
    type_name = 'B_SPLINE_CURVE_WITH_KNOTS'

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
    knot_mult    = {self.knot_multiplicities}
    knots        = {self.knots}
    knot_spec    = {self.knot_spec}'''
    
    def __get_arguments(self, conn):
        args = get_complex_or_base_arguments(conn,
                                             self.key,
                                             ['REPRESENTATION_ITEM',
                                              'GEOMETRIC_REPRESENTATION_ITEM',
                                              'CURVE',
                                              'BOUNDED_CURVE',
                                              'B_SPLINE_CURVE',
                                              'B_SPLINE_CURVE_WITH_KNOTS'])
        
        self.knot_multiplicities = args[6]
        self.knots = args[7]
        self.knot_spec = args[8]
        
    def get_geometry(self):
        return super().get_geometry() | {
            'type': self.type_name,
            'knot_mult': [int(v) for v in self.knot_multiplicities],
            'pts': [float(v) for v in self.knots],
            'spec': self.knot_spec
        }