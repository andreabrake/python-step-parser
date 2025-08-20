from .helpers import get_arguments, clean_display, ChildTypeRegister
from . import transient
from . import product_definition_formation
from . import abstract_types

type_name = 'PROPERTY_DEFINITION'
class PropertyDefinition(transient.Transient):
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
    name         = {self.name}
    description  = {self.description}
    definition   = {clean_display(self.definition)}'''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        
        self.name = args[0]
        self.description = args[1]
        self.definition = abstract_types.characterized_definition_register.parse(conn, args[2])

child_type_register = ChildTypeRegister(type_name, transient.child_type_register)
child_type_register.register(type_name, lambda conn, key: PropertyDefinition(conn, key))