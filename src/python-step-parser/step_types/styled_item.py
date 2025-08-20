from .helpers import get_arguments, clean_display, clean_display_list, ChildTypeRegister
from .presentation_style_assignment import PresentationStyleAssignment
from . import representation_item
from . import transient

type_name = 'STYLED_ITEM'

class StyledItem(representation_item.RepresentationItem):
    type_name = type_name

    def __init__(self, conn, key: int):
        super().__init__(conn, key)
        self.__get_arguments(conn)

    def __str__(self):
        return f'''{self.type_name} (
{self._str_args()}
)
'''
    
    def _str_args(self):
        return f'''{super()._str_args()}
    styles       = {clean_display_list(self.styles)}
    item         = {clean_display(self.item)}'''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        self.styles = [PresentationStyleAssignment(conn, e) for e in args[1]]
        self.item = transient.child_type_register.parse(conn, args[2])


child_type_register = ChildTypeRegister(type_name, representation_item.child_type_register)
child_type_register.register(type_name, lambda conn, key: StyledItem(conn, key))