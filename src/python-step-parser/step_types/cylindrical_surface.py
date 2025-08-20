from .helpers import get_arguments, clean_display
from .elementary_surface import ElementarySurface
from ..step_parser import StepParser

class CylindricalSurface(ElementarySurface):
    type_name = 'CYLINDRICAL_SURFACE'

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
    radius       = {self.radius}'''
    
    def __get_arguments(self, parser: StepParser):
        args = parser.get_arguments(self.key)
        self.radius = args[2]
        
    def get_geometry(self):
        return super().get_geometry() | {
            'type': 'CYLINDRICAL',
            'radius': self.radius
        }