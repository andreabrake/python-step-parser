from step_types.helpers import get_complex_or_base_arguments
from step_types.named_unit import NamedUnit

class SIUnit(NamedUnit):
    def __init__(self, conn, key: int):
        super().__init__(conn, key)
        self.__get_arguments(conn)

    def __str__(self):
        return f'''SI_UNIT (
{self._str_args()}
)
'''
    
    def _str_args(self):
        return f'''{super()._str_args()}
    prefix       = {self.prefix}
    name         = {self.name}'''

    def __get_arguments(self, conn):
        args = get_complex_or_base_arguments(conn,
                                             self.key,
                                             ['NAMED_UNIT',
                                              'SI_UNIT'])
        
        self.prefix = args[1]
        self.name = args[2]
