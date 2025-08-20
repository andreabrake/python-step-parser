from .helpers import get_arguments, clean_display
from . import placement
from .direction import Direction

type_name = 'AXIS2_PLACEMENT_3D'
class Axis2Placement3d(placement.Placement):
    def __init__(self, conn, key: int):
        super().__init__(conn, key)
        self.__get_arguments(conn)

    def __str__(self):
        return f'''{type_name} (
{self._str_args()}
)
'''
    
    def _str_args(self):
        return f'''{super()._str_args()}
    axis         = {clean_display(self.axis)}
    direction    = {clean_display(self.direction)}'''

    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        
        self.axis = Direction(conn, args[2])
        self.direction = Direction(conn, args[3])
    
    def get_geometry(self):
        return {
            'location': self.location.get_geometry(),
            'axis': self.axis.get_geometry(),
            'direction': self.direction.get_geometry(),
        }
    
placement.child_type_register.register(type_name, lambda conn, key: Axis2Placement3d(conn, key))