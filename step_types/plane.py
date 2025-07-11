from step_types.helpers import get_arguments, clean_display
from step_types.axis2_placement3d import Axis2Placement3d

class Plane():
    def __init__(self, conn, key: int):
        self.key = key
        self.__get_arguments(conn)
        pass

    def __str__(self):
        return f'''PLANE (
    key          = {self.key}
    name         = {self.name}
    position     = {clean_display(self.position)}
)
'''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        self.name = args[0]
        self.position = Axis2Placement3d(conn, args[1])