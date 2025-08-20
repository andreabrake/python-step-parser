from .product_definition import ProductDefinition

class StructuralResponseProperty(ProductDefinition):
    def __init__(self, conn, key: int):
        super().__init__(conn, key)
        self.__get_arguments(conn)

    def __str__(self):
        return f'''STRUCTURAL_RESPONSE_PROPERTY (
{self._str_args()}    
)
'''
    
    def _str_args(self):
        return f'''{super()._str_args()}'''
    
    def __get_arguments(self, conn):
        # No special arguments
        pass