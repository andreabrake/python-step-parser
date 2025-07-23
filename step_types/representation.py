from .helpers import get_arguments, clean_display, clean_display_list
from .abstract_types import representation_item, context
from .transient import Transient

class Representation(Transient):
    type_name = 'SHAPE_REPRESENTATION'

    def __init__(self, conn, key: int, resolve_children: bool = True):
        super().__init__(conn, key, resolve_children)
        self.__get_arguments(conn)

    def __str__(self):
        return f'''{self.type_name} (
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
            self.items = [representation_item.parse(conn, a) for a in args[1]]
        else:
            self.items = args[1]
        
        self.context = context.parse(conn, args[2])