from .helpers import get_arguments, clean_display_list
from .cartesian_point import CartesianPoint
from .loop import Loop

class PolyLoop(Loop):
    type_name = 'POLY_LOOP'

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
    polygon      = {clean_display_list(self.polygon)}'''

    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        self.polygon = [CartesianPoint(conn, p) for p in args[1]]