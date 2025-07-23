from .helpers import get_arguments, clean_display_list
from .surface_style_fill_area import SurfaceStyleFillArea
from .abstract_types import surface_style

class SurfaceSideStyle():
    def __init__(self, conn, key: int):
        self.key = key
        self.__get_arguments(conn)
        pass

    def __str__(self):
        return f'''SURFACE_SIDE_STYLE (
    key          = {self.key}
    side         = {self.side}
    styles       = {clean_display_list(self.styles)}
)
'''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        self.side = args[0]
        self.styles = [surface_style.parse(conn, e) for e in args[1]]