from .helpers import get_arguments, ChildTypeRegister
from . import application_context_element

type_name = 'PRODUCT_CONTEXT'
class ProductContext(application_context_element.ApplicationContextElement):
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
    discipline   = {self.discipline}'''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        self.discipline = args[2]

child_type_register = ChildTypeRegister(type_name, application_context_element.child_type_register)
child_type_register.register(type_name, lambda conn, key: ProductContext(conn, key))