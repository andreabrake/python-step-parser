from step_types.helpers import get_arguments, clean_display
from step_types.abstract_types import loop
from step_types.topological_representation_item import TopologicalRepresentationItem

class FaceBound(TopologicalRepresentationItem):
    type_name = 'FACE_BOUND'

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
    bound        = {clean_display(self.bound)}
    orientation  = {self.orientation}'''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        self.bound = loop.parse(conn, args[1])
        self.orientation = args[2]
    
    def get_geometry(self):
        return super().get_geometry() | {
            'type': self.type_name,
            'bound': self.bound.get_geometry(),
            'orientation': self.orientation
        }