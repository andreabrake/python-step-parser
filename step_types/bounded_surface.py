from step_types.helpers import get_arguments, clean_display
from step_types.surface import Surface

class BoundedSurface(Surface):
    type_name = 'BOUNDED_SURFACE'

    def __init__(self, conn, key: int):
        super().__init__(conn, key)
        self.__get_arguments(conn)

    def __str__(self):
        return f'''{self.type_name} (
{self._str_args()}
)
'''

    def _str_args(self):
        return f'''{super()._str_args()}'''
    
    def __get_arguments(self, conn):
        pass

    def get_geometry(self):
        return {
            'type': 'BOUNDED'
        }