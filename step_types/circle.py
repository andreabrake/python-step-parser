from step_types.helpers import get_arguments, clean_display
from step_types.conic import Conic

class Circle(Conic):
    type_name = 'CIRCLE'

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
    radius       = {self.radius}'''

    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        self.radius = args[2]
        
    def get_geometry(self):
        return super().get_geometry() | {
            'type': self.type_name,
            'radius': self.radius,
        }