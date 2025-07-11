from parsers.helpers import get_arguments, clean_display
from parsers.closed_shell import ClosedShell

class ManifoldSolidBrep():
    def __init__(self, conn, key: int):
        self.key = key
        self.__get_arguments(conn)
        pass

    def __str__(self):
        return f'''MANIFOLD_SOLID_BREP (
    key          = {self.key}
    name         = {self.name}
    outer        = {clean_display(self.outer)}
)
'''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        self.name = args[0]
        self.outer = ClosedShell(conn, args[1])