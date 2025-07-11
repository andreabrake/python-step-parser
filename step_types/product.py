from step_types.helpers import get_arguments, clean_display_list
from step_types.product_context import ProductContext

class Product():
    def __init__(self, conn, key: int):
        self.key = key
        self.__get_arguments(conn)
        pass

    def __str__(self):
        return f'''PRODUCT (
    key          = {self.key}
    id           = {self.id}
    name         = {self.name}
    description  = {self.description}
    product_ctxs = {clean_display_list(self.product_contexts)}
)
'''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        self.id = args[0]
        self.name = args[1]
        self.description = args[2]
        self.frame_of_reference = args[3]
        
        self.product_contexts = self.__get_product_contexts(conn)

    def __get_product_contexts(self, conn):
        return [ProductContext(conn, r) for r in self.frame_of_reference]
            