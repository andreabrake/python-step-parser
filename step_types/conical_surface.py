from .helpers import get_arguments, clean_display
from .elementary_surface import ElementarySurface

class ConicalSurface(ElementarySurface):
    type_name = 'CONICAL_SURFACE'

    def __init__(self, conn, key: int):
        super().__init__(conn, key)
        self.__get_arguments(conn)

    def __str__(self):
        return f'''{self.type_name} (
{self._str_args()}
)
'''

    def _str_args(self):
        return f'''{super()._str_args()}
    radius       = {self.radius}
    semi_angle   = {self.semi_angle}'''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        self.radius = args[2]
        self.semi_angle = args[3]