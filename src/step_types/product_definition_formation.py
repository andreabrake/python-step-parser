from .helpers import get_arguments, clean_display, ChildTypeRegister
from . import transient
from . import product

type_name: str = 'PRODUCT_DEFINITION_FORMATION'
class ProductDefinitionFormation(transient.Transient):
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
    id           = {self.id}
    description  = {self.description}
    product      = {clean_display(self.product)}'''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        
        self.id = args[0]
        self.description = args[1]
        self.product = product.child_type_register.parse(conn, args[2])

child_type_register = ChildTypeRegister(type_name, transient.child_type_register)
child_type_register.register(type_name, lambda conn, key: ProductDefinitionFormation(conn, key))
