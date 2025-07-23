from .helpers import get_arguments, clean_display
from .cartesian_point import CartesianPoint
from .vector import Vector
from .curve import Curve

class Line(Curve):
    type_name = 'LINE'

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
    point        = {clean_display(self.point)}
    direction    = {clean_display(self.direction)}'''

    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        self.point = CartesianPoint(conn, args[1])
        self.direction = Vector(conn, args[2])
        
    def get_geometry(self):
        return super().get_geometry() | {
            'type': self.type_name,
            'point': self.point.get_geometry(),
            'dir': self.direction.get_geometry(),
        }