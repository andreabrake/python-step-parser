from step_types.helpers import get_arguments, clean_display
from step_types.edge_curve import EdgeCurve

class OrientedEdge():
    def __init__(self, conn, key: int):
        self.key = key
        self.__get_arguments(conn)
        pass

    def __str__(self):
        return f'''ORIENTED_EDGE (
    key          = {self.key}
    name         = {self.name}
    edge_element = {clean_display(self.edge_element)}
    orientation  = {self.orientation}
)
'''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        self.name = args[0]
        self.edge_element = EdgeCurve(conn, args[3])
        self.orientation = args[4]