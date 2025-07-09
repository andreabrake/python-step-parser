from parsers.helpers import get_arguments, clean_display
from parsers.axis2_placement3d import Axis2Placement3d

class Circle():
    def __init__(self, conn, key: int):
        self.key = key
        self.__get_arguments(conn)
        pass

    def __str__(self):
        return f'''CIRCLE (
    key          = {self.key}
    name         = {self.name}
    position     = {clean_display(self.position)}
    radius       = {self.radius}
)
'''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        self.name = args[0]
        self.position = Axis2Placement3d(conn, args[1])
        self.radius = args[2]