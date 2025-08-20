from .helpers import get_arguments, clean_display_list, ChildTypeRegister
from . import transient
from . import product_context

type_name: str = 'PRODUCT'

class Product(transient.Transient):
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
    name         = {self.name}
    description  = {self.description}
    product_ctxs = {clean_display_list(self.product_contexts)}'''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        
        self.id = args[0]
        self.name = args[1]
        self.description = args[2]
        self.product_contexts = [product_context.child_type_register.parse(conn, i) for i in args[3]]

child_type_register = ChildTypeRegister(type_name, transient.child_type_register)
child_type_register.register(type_name, lambda conn, key: Product(conn, key))