from .helpers import get_arguments, clean_display, clean_display_list

class Transient():
    type_name: str = 'TRANSIENT'

    def __init__(self, conn, key: int):
        self.key = key

    def __str__(self):
        return f'''{self.type_name} (
{self._str_args()}
)
'''
    def _str_args(self):
        return f'''    key          = {self.key}'''
    
    def __get_arguments(self, conn):
        pass
    
    def get_geometry(self):
        return {}