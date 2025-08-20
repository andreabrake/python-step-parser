from .helpers import get_arguments, clean_display
from .vertex_point import VertexPoint
from .loop import Loop
from ..step_parser import StepParser

class VertexLoop(Loop):
    type_name = 'VERTEX_LOOP'

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
    vertex       = {clean_display(self.vertex)}'''

    def __get_arguments(self, parser: StepParser):
        args = parser.get_arguments(self.key)
        self.vertex = VertexPoint(parser, args[1])