from step_types.helpers import get_arguments, clean_display
from step_types.axis2_placement3d import Axis2Placement3d

class ToroidalSurface():
    def __init__(self, conn, key: int):
        self.key = key
        self.__get_arguments(conn)
        pass

    def __str__(self):
        return f'''TOROIDAL_SURFACE (
    key          = {self.key}
    name         = {self.name}
    position     = {clean_display(self.position)}
    major_radius = {self.major_radius}
    minor_radius = {self.minor_radius}
)
'''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        self.name = args[0]
        self.position = Axis2Placement3d(conn, args[1])
        self.major_radius = args[2]
        self.minor_radius = args[3]