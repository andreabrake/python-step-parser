from .helpers import get_complex_or_base_arguments, clean_display_list
from .b_spline_curve import BSPlineCurve

class RationalBSplineCurve(BSPlineCurve):
    type_name = 'RATIONAL_B_SPLINE_CURVE'

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
    weights      = {self.weights}'''

    
    def __get_arguments(self, conn):
        args = get_complex_or_base_arguments(conn,
                                             self.key,
                                             ['REPRESENTATION_ITEM',
                                              'GEOMETRIC_REPRESENTATION_ITEM',
                                              'CURVE',
                                              'BOUNDED_CURVE',
                                              'B_SPLINE_CURVE',
                                              'RATIONAL_B_SPLINE_CURVE'])
        
        self.weights = args[6]

    def get_geometry(self):
        return super().get_geometry() | {
            'type': self.type_name,
            'weights': [float(v) for v in self.weights]
        }