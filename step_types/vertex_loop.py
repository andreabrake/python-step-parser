from parsers.helpers import get_arguments, clean_display
from parsers.vertex_point import VertexPoint

class VertexPoint():
    def __init__(self, conn, key: int):
        self.key = key
        self.__get_arguments(conn)
        pass

    def __str__(self):
        return f'''VERTEX_POINT (
    key          = {self.key}
    name         = {self.name}
    vertex       = {clean_display(self.vertex)}
)
'''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        self.name = args[0]
        self.vertex = VertexPoint(conn, args[1])