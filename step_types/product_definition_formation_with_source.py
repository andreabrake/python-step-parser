from step_types.helpers import get_arguments, clean_display, clean_display_list
from step_types.product_definition_formation import ProductDefinitionFormation

class ProductDefinitionFormationWithSource(ProductDefinitionFormation):
    def __init__(self, conn, key: int):
        super().__init__(conn, key)
        self.__get_arguments(conn)

    def __str__(self):
        return f'''PRODUCT_DEFINITION_FORMATION_WITH_SPECIFIED_SOURCE (
{self._str_args()}
)
'''
    
    def _str_args(self):
        return f'''{super()._str_args()}
    source       = {self.source}'''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        
        self.source = args[3]