from .helpers import get_arguments, clean_display
from .axis2_placement3d import Axis2Placement3d

class SphericalSurface():
    type_name = 'SPHERICAL_SURFACE'

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