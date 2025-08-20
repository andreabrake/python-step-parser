from .helpers import get_arguments, clean_display
from .fill_area_style import FillAreaStyle
from ..step_parser import StepParser

class SurfaceStyleFillArea():
    def __init__(self, parser: StepParser, key: int):
        self.key = key
        self.__get_arguments(parser)
        pass

    def __str__(self):
        return f'''SURFACE_STYLE_FILL_AREA (
    key          = {self.key}
    fill_area    = {clean_display(self.fill_area)}
)
'''
    
    def __get_arguments(self, parser: StepParser):
        args = parser.get_arguments(self.key)
        self.fill_area = FillAreaStyle(parser, args[0])