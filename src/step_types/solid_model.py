from .helpers import get_arguments, clean_display, ChildTypeRegister
from . import geometric_representation_item
from . import property_definition
from . import shape_representation

type_name = 'SOLID_MODEL'
class SolidModel(geometric_representation_item.GeometricRepresentationItem):
    type_name = type_name

    def __init__(self, conn, key: int, resolve_children: bool = False):
        super().__init__(conn, key, resolve_children)
        self.__get_arguments(conn)

    def __str__(self):
        return f'''{type_name} (
{self._str_args()}
)
'''
    
    def _str_args(self):
        return f'''{super()._str_args()}'''

    def __get_arguments(self, conn):
        pass

child_type_register = ChildTypeRegister(type_name, geometric_representation_item.child_type_register)
child_type_register.register(type_name, lambda conn, key: SolidModel(conn, key))