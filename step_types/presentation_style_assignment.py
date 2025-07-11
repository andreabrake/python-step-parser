from step_types.helpers import get_arguments, clean_display_list
from step_types.surface_style_usage import SurfaceStyleUsage

class PresentationStyleAssignment():
    def __init__(self, conn, key: int):
        self.key = key
        self.__get_arguments(conn)
        pass

    def __str__(self):
        return f'''PRESENTATION_STYLE_ASSIGNMENT (
    key          = {self.key}
    styles       = {clean_display_list(self.styles)}
)
'''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        self.styles = [SurfaceStyleUsage(conn, e) for e in args[0]]