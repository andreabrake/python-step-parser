from .helpers import get_arguments, clean_display_list
from .oriented_edge import OrientedEdge
from .loop import Loop
from ..step_parser import StepParser

class EdgeLoop(Loop):
    type_name = 'EDGE_LOOP'

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
    edge_list    = {clean_display_list(self.edge_list)}'''

    
    def __get_arguments(self, parser: StepParser):
        args = parser.get_arguments(self.key)
        self.edge_list = [OrientedEdge(parser, e) for e in args[1]]

    def get_geometry(self):
        return super().get_geometry() | {
            'type': self.type_name,
            'edges': [e.get_geometry() for e in self.edge_list]
        }