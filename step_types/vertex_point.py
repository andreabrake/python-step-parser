from step_types.helpers import get_arguments, clean_display
from step_types.cartesian_point import CartesianPoint

class VertexPoint():
    def __init__(self, conn, key: int):
        self.key = key
        self.__get_arguments(conn)
        pass

    def __str__(self):
        return f'''VERTEX_POINT (
    key          = {self.key}
    name         = {self.name}
    geometry     = {clean_display(self.geometry)}
)
'''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        self.name = args[0]
        self.geometry = CartesianPoint(conn, args[1])

    def get_geometry(self): 
        return self.geometry.get_geometry()