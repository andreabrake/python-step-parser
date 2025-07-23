from .helpers import get_arguments, clean_display
from .conic import Conic

class Hyperbola(Conic):
    type_name = 'HYPERBOLA'

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
    semi_axis    = {self.semi_axis}
    semi_axis_i  = {self.semi_imag_axis}'''

    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        self.semi_axis = args[2]
        self.semi_imag_axis = args[3]

    def get_geometry(self):
        return super().get_geometry() | {
            'type': self.type_name,
            'axes': [self.semi_axis, self.semi_imag_axis],
        }