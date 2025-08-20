from .helpers import get_arguments, clean_display, clean_display_list, ChildTypeRegister
from . import representation_item
from . import transient
from . import representation_context

type_name = 'REPRESENTATION'
class Representation(transient.Transient):
    type_name = type_name
    def __init__(self, conn, key: int, resolve_children: bool = False):
        super().__init__(conn, key, resolve_children)
        self.__get_arguments(conn)

    def __str__(self):
        return f'''{type_name} (
{self._str_args()}
)
'''
    
    def _str_args(self):
        return f'''{super()._str_args()}
    name         = {self.name}
    items        = {clean_display_list(self.items) if self.resolve_children else self.items}
    context      = {clean_display(self.context) if self.resolve_children else self.context}'''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)

        self.name = args[0]
        if self.resolve_children:
            self.items = [representation_item.child_type_register.parse(conn, a) for a in args[1]]
        else:
            self.items = args[1]
        
        self.context = representation_context.child_type_register.parse(conn, args[2])

child_type_register = ChildTypeRegister(type_name, transient.child_type_register)
child_type_register.register(type_name, lambda conn, key: Representation(conn, key))