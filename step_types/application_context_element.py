from .helpers import get_arguments, ChildTypeRegister
from . import transient 
from . import application_context

type_name = 'APPLICATION_CONTEXT_ELEMENT'
class ApplicationContextElement(transient.Transient):
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
    name         = {self.name}'''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        
        self.name = args[0]
        self.context = application_context.child_type_register.parse(conn, args[1])

child_type_register = ChildTypeRegister(type_name, transient.child_type_register)
child_type_register.register(type_name, lambda conn, key: ApplicationContextElement(conn, key))
