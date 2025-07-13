from step_types.helpers import get_arguments, clean_display
from step_types.abstract_types import loop

class FaceBound():
    def __init__(self, conn, key: int):
        self.key = key
        self.__get_arguments(conn)
        pass

    def __str__(self):
        return f'''FACE_BOUND (
    key          = {self.key}
    name         = {self.name}
    bound        = {clean_display(self.bound)}
    orientation  = {self.orientation}
)
'''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        self.name = args[0]
        self.bound = loop.parse(conn, args[1])
        self.orientation = args[2]