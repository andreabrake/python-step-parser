from step_types.helpers import get_arguments
from step_types.colour_rgb import ColourRGB

class DraughtingPreDefinedColour():
    def __init__(self, conn, key: int):
        self.key = key
        self.__get_arguments(conn)
        pass

    def __str__(self):
        return f'''DRAUGHTING_PRE_DEFINED_COLOUR (
    key          = {self.key}
    name         = {self.name}
)
'''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        self.name = args[0]