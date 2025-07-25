from .helpers import get_arguments, clean_display, clean_display_list
from .product_definition import ProductDefinition

class ProductDefinitionShape(ProductDefinition):
    def __init__(self, conn, key: int):
        super().__init__(conn, key)
        self.__get_arguments(conn)

    def __str__(self):
        return f'''PRODUCT_DEFINITION_SHAPE (
{self._str_args()}
)
'''
    
    def _str_args(self):
        return f'''{super()._str_args()}'''
    
    def __get_arguments(self, conn):
        # No special arguments
        pass