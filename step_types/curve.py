from .helpers import get_complex_or_base_arguments, ChildTypeRegister
from . import geometric_representation_item

type_name = 'CURVE'

class Curve(geometric_representation_item.GeometricRepresentationItem):
    type_name = type_name

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
        args = get_complex_or_base_arguments(conn,
                                             self.key,
                                             ['REPRESENTATION_ITEM',
                                              'GEOMETRIC_REPRESENTATION_ITEM',
                                              'CURVE'])
        pass

    
child_type_register = ChildTypeRegister(type_name, geometric_representation_item.child_type_register)
child_type_register.register(type_name, lambda conn, key: Curve(conn, key))