from .helpers import get_arguments, clean_display
from .surface_side_style import SurfaceSideStyle

class SurfaceStyleUsage():
    def __init__(self, conn, key: int):
        self.key = key
        self.__get_arguments(conn)
        pass

    def __str__(self):
        return f'''SURFACE_STYLE_USAGE (
    key          = {self.key}
    side         = {self.side}
    style        = {clean_display(self.style)}
)
'''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        self.side = args[0]
        self.style = SurfaceSideStyle(conn, args[1])