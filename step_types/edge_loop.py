from step_types.helpers import get_arguments, clean_display_list
from step_types.oriented_edge import OrientedEdge
from step_types.loop import Loop

class EdgeLoop(Loop):
    type_name = 'EDGE_LOOP'

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
    edge_list    = {clean_display_list(self.edge_list)}'''

    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        self.edge_list = [OrientedEdge(conn, e) for e in args[1]]

    def get_geometry(self):
        return super().get_geometry() | {
            'type': self.type_name,
            'edges': [e.get_geometry() for e in self.edge_list]
        }