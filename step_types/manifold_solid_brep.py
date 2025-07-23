from .helpers import get_arguments, clean_display
from .closed_shell import ClosedShell
from .transient import Transient

class ManifoldSolidBrep(Transient):
    type_name = 'MANIFOLD_SOLID_BREP'

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
    name         = {self.name}
    outer        = {clean_display(self.outer)}'''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        self.name = args[0]
        self.outer = ClosedShell(conn, args[1])