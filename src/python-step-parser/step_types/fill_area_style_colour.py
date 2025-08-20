from .helpers import get_arguments, clean_display
from .abstract_types import color

class FillAreaStyleColour():
    def __init__(self, conn, key: int):
        self.key = key
        self.__get_arguments(conn)
        pass

    def __str__(self):
        return f'''FILL_AREA_STYLE_COLOUR (
    key          = {self.key}
    name         = {self.name}
    colour       = {clean_display(self.colour)}
)
'''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        self.name = args[0]
        self.colour = color.parse(conn, args[1])