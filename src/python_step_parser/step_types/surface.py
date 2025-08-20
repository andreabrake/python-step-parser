from .helpers import get_complex_or_base_arguments
from .geometric_representation_item import GeometricRepresentationItem
from ..step_parser import StepParser

class Surface(GeometricRepresentationItem):
    def __init__(self, parser: StepParser, key: int):
        super().__init__(parser, key)
        self.__get_arguments(parser)

    def __str__(self):
        return f'''SURFACE (
{self._str_args()}
)
'''
    
    def _str_args(self):
        return f'''{super()._str_args()}'''
    
    def __get_arguments(self, parser: StepParser):
        pass