from .helpers import get_arguments, clean_display, clean_display_list
from .transient import Transient 
from .product import Product

class ProductDefinitionFormation(Transient):
    def __init__(self, conn, key: int):
        super().__init__(conn, key)
        self.__get_arguments(conn)

    def __str__(self):
        return f'''PRODUCT_DEFINITION_FORMATION (
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
        self.product = Product(conn, args[2])