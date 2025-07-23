from step_types.helpers import get_arguments, clean_display
from step_types.elementary_surface import ElementarySurface

class ToroidalSurface(ElementarySurface):
    type_name = 'TOROIDAL_SURFACE'

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
    major_radius = {self.major_radius}
    minor_radius = {self.minor_radius}'''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        self.major_radius = args[2]
        self.minor_radius = args[3]