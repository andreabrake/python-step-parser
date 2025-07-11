from step_types.helpers import get_arguments, clean_display_list
from step_types.oriented_edge import OrientedEdge

class EdgeLoop():
    def __init__(self, conn, key: int):
        self.key = key
        self.__get_arguments(conn)
        pass

    def __str__(self):
        return f'''EDGE_LOOP (
    key          = {self.key}
    name         = {self.name}
    edge_list    = {clean_display_list(self.edge_list)}
)
'''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        self.name = args[0]
        self.edge_list = [OrientedEdge(conn, e) for e in args[1]]