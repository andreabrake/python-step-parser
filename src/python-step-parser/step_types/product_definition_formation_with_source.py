from .helpers import get_arguments, ChildTypeRegister
from . import product_definition_formation

type_name: str = 'PRODUCT_DEFINITION_FORMATION_WITH_SPECIFIED_SOURCE'
class ProductDefinitionFormationWithSource(product_definition_formation.ProductDefinitionFormation):
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
    source       = {self.source}'''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        
        self.source = args[3]

child_type_register = ChildTypeRegister(type_name, product_definition_formation.child_type_register)
child_type_register.register(type_name, lambda conn, key: ProductDefinitionFormationWithSource(conn, key))
