from .helpers import get_arguments
from .point import Point

class CartesianPoint(Point):
    type_name = 'CARTESIAN_POINT'

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
    coordinates  = {self.coordinates}'''

    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        self.name = args[0]
        self.coordinates = args[1]
        
    def get_geometry(self):
        x,y,z = self.coordinates
        return [float(x), float(y), float(z)]