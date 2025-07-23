from step_types.helpers import get_arguments, clean_display
from step_types.cartesian_point import CartesianPoint
from step_types.topological_representation_item import TopologicalRepresentationItem

class Vertex(TopologicalRepresentationItem):
    type_name = 'VERTEX'

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
    geometry     = {clean_display(self.geometry)}'''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        self.geometry = CartesianPoint(conn, args[1])

    def get_geometry(self): 
        return self.geometry.get_geometry()