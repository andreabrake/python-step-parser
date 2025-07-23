from step_types.helpers import get_arguments, clean_display
from step_types.conic import Conic

class Parabola(Conic):
    type_name = 'PARABOLA'

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
    focal_dist   = {self.focal_distance}'''

    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        self.focal_distance = args[2]
        
    def get_geometry(self):
        return super().get_geometry() | {
            'type': self.type_name,
            'focal_distance': self.focal_distance,
        }