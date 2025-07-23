from .helpers import get_arguments, clean_display
from .fill_area_style import FillAreaStyle

class SurfaceStyleFillArea():
    def __init__(self, conn, key: int):
        self.key = key
        self.__get_arguments(conn)
        pass

    def __str__(self):
        return f'''SURFACE_STYLE_FILL_AREA (
    key          = {self.key}
    fill_area    = {clean_display(self.fill_area)}
)
'''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        self.fill_area = FillAreaStyle(conn, args[0])