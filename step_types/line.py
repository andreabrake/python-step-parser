from step_types.helpers import get_arguments, clean_display
from step_types.cartesian_point import CartesianPoint
from step_types.vector import Vector

class Line():
    def __init__(self, conn, key: int):
        self.key = key
        self.__get_arguments(conn)
        pass

    def __str__(self):
        return f'''LINE (
    key          = {self.key}
    name         = {self.name}
    point        = {clean_display(self.point)}
    direction    = {clean_display(self.direction)}
)
'''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        self.name = args[0]
        self.point = CartesianPoint(conn, args[1])
        self.direction = Vector(conn, args[2])