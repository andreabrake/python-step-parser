from .helpers import get_arguments
from .b_spline_surface import BSPlineSurface
from ..step_parser import StepParser

class BSplineSurfaceWithKnots(BSPlineSurface):
    type_name = 'B_SPLINE_SURFACE_WITH_KNOTS'

    def __init__(self, parser: StepParser, key: int):
        super().__init__(parser, key)
        self.__get_arguments(parser)

    def __str__(self):
        return f'''{self.type_name} (
{self._str_args()}
)
'''

    def _str_args(self):
        return f'''{super()._str_args()}
    umults       = {self.umultiplicities}
    vmults       = {self.vmultiplicities}
    uknots       = {self.uknots}
    vknots       = {self.vknots}
    knot_spec    = {self.knot_spec}'''

    
    def __get_arguments(self, parser: StepParser):
        args = parser.get_arguments(self.key)

        self.umultiplicities = args[8]
        self.vmultiplicities = args[9]
        self.uknots = args[10]
        self.vknots = args[11]
        self.knot_spec = args[12]