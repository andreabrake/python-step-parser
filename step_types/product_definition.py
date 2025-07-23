from .helpers import get_arguments, clean_display, clean_display_list
from .abstract_types import characterized_definition
from .transient import Transient

class ProductDefinition(Transient):
    def __init__(self, conn, key: int):
        super().__init__(conn, key)
        self.__get_arguments(conn)

    def __str__(self):
        return f'''PRODUCT_DEFINITION (
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
        self.definition = characterized_definition.parse(conn, args[2])