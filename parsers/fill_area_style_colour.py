from parsers.helpers import get_arguments
from parsers.abstract_parsers.parse_colour import parse_colour

class FillAreaStyleColour():
    def __init__(self, conn, key: int):
        self.key = key
        self.__get_arguments(conn)
        pass

    def __str__(self):
        return f'''FILL_AREA_STYLE_COLOUR (
    key          = {self.key}
    name         = {self.name}
    colour       = {self.colour}
)
'''
    
    def __get_arguments(self, conn):
        print('fill area key', self.key)
        args = get_arguments(conn, self.key)
        self.name = args[0]
        self.colour = parse_colour(conn, args[1])