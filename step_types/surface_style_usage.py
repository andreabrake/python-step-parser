from parsers.helpers import get_arguments, clean_display_list
from parsers.surface_side_style import SurfaceSideStyle

class SurfaceStyleUsage():
    def __init__(self, conn, key: int):
        self.key = key
        self.__get_arguments(conn)
        pass

    def __str__(self):
        return f'''SURFACE_STYLE_USAGE (
    key          = {self.key}
    name         = {self.name}
    style        = {clean_display_list(self.style)}
)
'''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        self.side = args[0]
        self.style = SurfaceSideStyle(conn, args[1])