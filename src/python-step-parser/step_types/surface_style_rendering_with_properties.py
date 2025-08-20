from .helpers import get_arguments, clean_display, clean_display_list
from .abstract_types import color
from .surfacer_style_transparent import SurfaceStyleTransparent

class SurfaceStyleRenderingWithProperties():
    def __init__(self, conn, key: int):
        self.key = key
        self.__get_arguments(conn)
        pass

    def __str__(self):
        return f'''SURFACE_STYLE_RENDERING_WITH_PROPERTIES (
    key          = {self.key}
    method       = {self.method}
    colour       = {clean_display(self.colour)}
    transparency = {clean_display_list(self.transparency)}
)
'''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        self.method = args[0]
        self.colour = color.parse(conn, args[1])
        self.transparency = [SurfaceStyleTransparent(conn, arg) for arg in args[2]]