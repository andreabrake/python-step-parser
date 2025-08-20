from .helpers import get_complex_or_base_arguments
from . import si_unit

class LengthUnit(si_unit.SIUnit):
    def __init__(self, conn, key: int):
        super().__init__(conn, key)
        self.__get_arguments(conn)

    def __str__(self):
        return f'''LENGTH_UNIT (
{self._str_args()}
)
'''
    
    def _str_args(self):
        return f'''{super()._str_args()}'''

    def __get_arguments(self, conn):
        args = get_complex_or_base_arguments(conn,
                                             self.key,
                                             ['NAMED_UNIT',
                                              'SI_UNIT',
                                              'LENGTH_UNIT'])
        # No extra params
        pass

si_unit.child_type_register.register('LENGTH_UNIT', lambda conn, key: LengthUnit(conn, key))