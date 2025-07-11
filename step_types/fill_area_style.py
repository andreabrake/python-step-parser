from step_types.helpers import get_arguments
from step_types.fill_area_style_colour import FillAreaStyleColour

class FillAreaStyle():
    def __init__(self, conn, key: int):
        self.key = key
        self.__get_arguments(conn)
        pass

    def __str__(self):
        return f'''FILL_AREA_STYLE (
    key          = {self.key}
    name         = {self.name}
    fill_styles  = {self.fill_styles}
)
'''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        self.name = args[0]
        self.fill_styles = [FillAreaStyleColour(conn, arg) for arg in args[1]]