from .helpers import ChildTypeRegister
from . import property_definition
from .abstract_types import characterized_definition_register

type_name = 'PRODUCT_DEFINITION_SHAPE'
class ProductDefinitionShape(property_definition.PropertyDefinition):
    def __init__(self, conn, key: int):
        super().__init__(conn, key)
        self.__get_arguments(conn)

    def __str__(self):
        return f'''{type_name} (
{self._str_args()}
)
'''
    
    def _str_args(self):
        return f'''{super()._str_args()}'''
    
    def __get_arguments(self, conn):
        # No special arguments
        pass

child_type_register = ChildTypeRegister(type_name, [
    property_definition.child_type_register,
    characterized_definition_register
])
child_type_register.register(type_name, lambda conn, key: ProductDefinitionShape(conn, key))