from step_types.helpers import get_arguments, clean_display, clean_display_list

class Transient():
    def __init__(self, conn, key: int):
        self.key = key

    def __str__(self):
        return f'''TRANSIENT (
{self._str_args()}
)
'''
    def _str_args(self):
        return f'''    key          = {self.key}'''
    
    def __get_arguments(self, conn):
        pass