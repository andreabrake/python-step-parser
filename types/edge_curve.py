from parsers.helpers import  get_arguments, clean_display
from parsers.vertex_point import VertexPoint
from parsers.abstract_parsers.curve import parse_curve

class EdgeCurve():
    def __init__(self, conn, key: int):
        self.key = key
        self.__get_arguments(conn)
        pass

    def __str__(self):
        return f'''EDGE_CURVE (
    key          = {self.key}
    name         = {self.name}
    start        = {clean_display(self.start)}
    end          = {clean_display(self.end)}
    geometry     = {clean_display(self.geometry)}
    same_sense   = {self.same_sense}
)
'''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        self.name = args[0]
        self.start = VertexPoint(conn, args[1])
        self.end = VertexPoint(conn, args[2])
        self.geometry = parse_curve(conn, args[3])
        self.same_sense = args[4]