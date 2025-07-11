from parsers.helpers import get_arguments, clean_display
from parsers.cartesian_point import CartesianPoint
from parsers.direction import Direction

class Axis2Placement3d():
    def __init__(self, conn, key: int):
        self.key = key
        self.__get_arguments(conn)
        pass

    def __str__(self):
        return f'''AXIS2_PLACEMENT_3D (
    key          = {self.key}
    name         = {self.name}
    location     = {clean_display(self.location)}
    axis         = {clean_display(self.axis)}
    direction    = {clean_display(self.direction)}
)
'''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        self.name = args[0]
        self.location = CartesianPoint(conn, args[1])
        self.axis = Direction(conn, args[2])
        self.direction = Direction(conn, args[2])