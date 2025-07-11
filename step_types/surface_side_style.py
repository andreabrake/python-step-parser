from step_types.helpers import get_arguments, clean_display_list
from step_types.surface_style_fill_area import SurfaceStyleFillArea

class SurfaceSideStyle():
    def __init__(self, conn, key: int):
        self.key = key
        self.__get_arguments(conn)
        pass

    def __str__(self):
        return f'''SURFACE_SIDE_STYLE (
    key          = {self.key}
    name         = {self.name}
    styles       = {clean_display_list(self.styles)}
)
'''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        self.side = args[0]
        self.styles = [SurfaceStyleFillArea(conn, e) for e in args[1]]