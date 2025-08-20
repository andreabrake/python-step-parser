from .helpers import get_arguments, clean_display
from . import application_context_element

class ProductDefinitionContext(application_context_element.ApplicationContextElement):
    def __init__(self, conn, key: int):
        super().__init__(conn, key)
        self.__get_arguments(conn)

    def __str__(self):
        return f'''PRODUCT_DEFINITION_CONTEXT (
{self._str_args()}
)
'''
    
    def _str_args(self):
        return f'''{super()._str_args()}
    stage        = {self.life_cycle_stage}'''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        
        self.life_cycle_stage = args[2]

application_context_element.register(
    'PRODUCT_DEFINITION_CONTEXT',
    lambda conn, key: ProductDefinitionContext(conn, key)
)
