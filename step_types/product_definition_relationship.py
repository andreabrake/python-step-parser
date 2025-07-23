from step_types.helpers import get_arguments, clean_display, clean_display_list
from step_types.transient import Transient

class ProductDefinitionRelationship(Transient):
    def __init__(self, conn, key: int):
        super().__init__(conn, key)
        self.__get_arguments(conn)

    def __str__(self):
        return f'''PRODUDCT_DEFINITION_RELATIONSHIP (
{self._str_args()}
)
'''
    
    def _str_args(self):
        return f'''{super()._str_args()}
    id           = {self.id}
    name         = {self.name}
    description  = {self.description}
    relating_def = {self.relating_product_definition}
    related_def  = {self.related_product_definition}'''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        
        self.id = args[0]
        self.name = args[1]
        self.description = args[2]
        self.relating_product_definition = args[3]
        self.related_product_definition = args[4]