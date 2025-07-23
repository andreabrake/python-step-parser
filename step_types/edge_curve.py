from step_types.helpers import  get_arguments, clean_display
from step_types.vertex_point import VertexPoint
from step_types.edge import Edge
from step_types.abstract_types.curve import parse_curve

class EdgeCurve(Edge):
    type_name = 'EDGE_CURVE'

    def __init__(self, conn, key: int):
        super().__init__(conn, key)
        self.__get_arguments(conn)

    def __str__(self):
        return f'''{self.type_name} (
{self._str_args()}
)
'''

    def _str_args(self):
        return f'''{super()._str_args()}
    start        = {clean_display(self.start)}
    end          = {clean_display(self.end)}
    geometry     = {clean_display(self.geometry)}
    same_sense   = {self.same_sense}'''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        self.start = VertexPoint(conn, args[1])
        self.end = VertexPoint(conn, args[2])
        self.geometry = parse_curve(conn, args[3])
        self.same_sense = args[4]

    def get_geometry(self):
        return super().get_geometry() | {
            'type': self.type_name,
            'start': self.start.get_geometry(),
            'end': self.end.get_geometry(),
            'curve': self.geometry.get_geometry(),
        }