from step_types.helpers import get_arguments, clean_display, clean_display_list
from step_types.product_definition_relationship import ProductDefinitionRelationship

class ProductDefinitionUsage(ProductDefinitionRelationship):
    def __init__(self, conn, key: int):
        super().__init__(conn, key)
        self.__get_arguments(conn)

    def __str__(self):
        return f'''PRODUCT_DEFINITION_USAGE (
    {self._str_args()}
)
'''
    
    def _str_args(self):
        return f'{super()._str_args()}'
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        
        # No additional args