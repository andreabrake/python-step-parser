from .helpers import get_arguments, clean_display
from .vertex_point import VertexPoint
from .loop import Loop

class VertexLoop(Loop):
    type_name = 'VERTEX_LOOP'

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
    vertex       = {clean_display(self.vertex)}'''

    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        self.vertex = VertexPoint(conn, args[1])