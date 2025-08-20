from .helpers import get_arguments, ChildTypeRegister
from . import transient

type_name = 'APPLICATION_CONTEXT'
class ApplicationContext(transient.Transient):
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
    application  = {self.application}'''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        
        self.application = args[0]

child_type_register = ChildTypeRegister(type_name, transient.child_type_register)
child_type_register.register(type_name, lambda conn, key: ApplicationContext(conn, key))
