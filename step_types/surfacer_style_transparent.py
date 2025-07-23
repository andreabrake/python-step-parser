from .helpers import get_arguments

class SurfaceStyleTransparent():
    def __init__(self, conn, key: int):
        self.key = key
        self.__get_arguments(conn)
        pass

    def __str__(self):
        return f'''SURFACE_STYLE_TRANSPARENT (
    key          = {self.key}
    transparency = {self.transparency}
)
'''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        self.transparency = args[0]