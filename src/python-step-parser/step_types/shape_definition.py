from .helpers import ChildTypeRegister
from . import transient

type_name = 'SHAPE_DEFINITION'
class ShapeDefinition(transient.Transient):
    def __init__(self, conn, key: int):
        self.key = key
        self.__get_arguments(conn)
        pass

    def __str__(self):
        return f'''{type_name} (
{self._str_args()}
)
'''
    
    def __get_arguments(self, conn):
        pass

        
child_type_register = ChildTypeRegister(type_name, transient.child_type_register)
child_type_register.register(type_name, lambda conn, key: ShapeDefinition(conn, key))