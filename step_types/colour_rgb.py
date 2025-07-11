from step_types.helpers import get_arguments

class ColourRGB():
    def __init__(self, conn, key: int):
        self.key = key
        self.__get_arguments(conn)
        pass

    def __str__(self):
        return f'''COLOUR_RGB (
    key          = {self.key}
    name         = {self.name}
    rgb          = ({self.r}, {self.g}, {self.b})
)
'''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        self.name = args[0]
        self.r = args[1]
        self.g = args[2]
        self.b = args[3]