from .helpers import get_arguments, clean_display
from .toroidal_surface import ToroidalSurface
from ..step_parser import StepParser

class DegenerateToroidalSurface(ToroidalSurface):
    type_name = 'DEGENERATE_TOROIDAL_SURFACE'

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
    select_outer = {self.select_outer}'''

    
    def __get_arguments(self, parser: StepParser):
        args = parser.get_arguments(self.key)
        self.select_outer = args[4]