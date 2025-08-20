from .helpers import get_arguments, clean_display
from .direction import Direction
from .geometric_representation_item import GeometricRepresentationItem

class Vector(GeometricRepresentationItem):
    type_name = 'VECTOR'

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
    orientation  = {clean_display(self.orientation)}
    magnitude    = {self.magnitude}'''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        self.orientation = Direction(conn, args[1])
        self.magnitude = args[2]

    def get_geometry(self):
        return super().get_geometry() | {
            'type': self.type_name,
            'orient': self.orientation.get_geometry(),
            'mag': self.magnitude
        }