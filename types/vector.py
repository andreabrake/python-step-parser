from parsers.helpers import get_arguments, clean_display
from parsers.direction import Direction

class Vector():
    def __init__(self, conn, key: int):
        self.key = key
        self.__get_arguments(conn)
        pass

    def __str__(self):
        return f'''VECTOR (
    key          = {self.key}
    name         = {self.name}
    orientation  = {clean_display(self.orientation)}
    magnitude    = {self.magnitude}
)
'''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        self.name = args[0]
        self.orientation = Direction(conn, args[1])
        self.magnitude = args[2]