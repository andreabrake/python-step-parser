from .helpers import get_complex_or_base_arguments, ChildTypeRegister
from . import transient

type_name = 'REPRESENTATION_ITEM'
class RepresentationItem(transient.Transient):
    type_name = type_name

    def __init__(self, conn, key: int, resolve_children: bool = False):
        super().__init__(conn, key, resolve_children)
        self.__get_arguments(conn)

    def __str__(self):
        return f'''{self.type_name} (
{self._str_args()}
)
'''
    
    def _str_args(self):
        return f'''{super()._str_args()}
    name         = {self.name}'''

    def __get_arguments(self, conn):
        args = get_complex_or_base_arguments(conn,
                                             self.key,
                                             ['REPRESENTATION_ITEM'])
        self.name = args[0]


child_type_register = ChildTypeRegister(type_name, transient.child_type_register)
child_type_register.register(type_name, lambda conn, key: RepresentationItem(conn, key))