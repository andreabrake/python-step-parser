from .helpers import get_arguments
from .representation_item import RepresentationItem
from ..step_parser import StepParser

class TopologicalRepresentationItem(RepresentationItem):
    def __init__(self, parser: StepParser, key: int):
        super().__init__(parser, key)
        self.__get_arguments(parser)

    def __str__(self):
        return f'''TOPOLOGICAL_REPRESENTATION_ITEM (
{self._str_args()}
)
'''
    
    def _str_args(self):
        return f'''{super()._str_args()}'''

    def __get_arguments(self, parser: StepParser):
        pass
