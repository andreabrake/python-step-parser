from .helpers import get_arguments, clean_display
from .edge_curve import EdgeCurve
from .edge import Edge

class OrientedEdge(Edge):
    type_name = 'ORIENTED_EDGE'

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
    edge_element = {clean_display(self.edge_element)}
    orientation  = {self.orientation}'''

    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        self.edge_element = EdgeCurve(conn, args[3])
        self.orientation = args[4]

    def get_geometry(self):
        return super().get_geometry() | {
            'type': self.type_name,
            'edge': self.edge_element.get_geometry(),
            'orientation': self.orientation
        }