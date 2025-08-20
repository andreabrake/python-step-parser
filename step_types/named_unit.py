from .helpers import get_complex_or_base_arguments, ChildTypeRegister
from . import transient
from .abstract_types import unit_register

type_name = 'NAMED_UNIT'
class NamedUnit(transient.Transient):
    def __init__(self, conn, key: int):
        super().__init__(conn, key)
        self.__get_arguments(conn)

    def __str__(self):
        return f'''{type_name} (
{self._str_args()}
)
'''
    
    def _str_args(self):
        return f'''{super()._str_args()}
    dimensions   = {self.dimensions}'''

    def __get_arguments(self, conn):
        args = get_complex_or_base_arguments(conn,
                                             self.key,
                                             ['NAMED_UNIT',])
        
        self.dimensions = args[0]

child_type_register = ChildTypeRegister(type_name, [
    transient.child_type_register,
    unit_register
])
child_type_register.register(type_name, lambda conn, key: NamedUnit(conn, key))