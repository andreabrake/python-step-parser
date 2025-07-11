from step_types.helpers import get_arguments, clean_display_list
from step_types.advanced_face import AdvancedFace

class ClosedShell():
    def __init__(self, conn, key: int):
        self.key = key
        self.__get_arguments(conn)
        pass

    def __str__(self):
        return f'''CLOSED_SHELL (
    key          = {self.key}
    name         = {self.name}
    faces        = {clean_display_list(self.faces)}
)
'''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        self.name = args[0]
        self.faces = [AdvancedFace(conn, arg) for arg in args[1]]