from .helpers import get_arguments, clean_display_list
from .advanced_face import AdvancedFace
from .transient import Transient

class ClosedShell(Transient):
    type_name = 'CLOSED_SHELL'

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
    faces        = {clean_display_list(self.faces)} '''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        self.name = args[0]
        self.faces = [AdvancedFace(conn, arg) for arg in args[1]]

    def get_geometry(self):
        return super().get_geometry() | {
            'faces': [f.get_geometry() for f in self.faces]
        }