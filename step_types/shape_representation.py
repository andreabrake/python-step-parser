from step_types.helpers import get_arguments, clean_display, clean_display_list
from step_types.abstract_types import representation_item, context
from step_types.representation import Representation

class ShapeRepresentation(Representation):
    def __init__(self, conn, key: int):
        super().__init__(conn, key)
        self.__get_arguments(conn)

    def __str__(self):
        return f'''SHAPE_REPRESENTATION (
{self._str_args()}
)
'''
    
    def __str__(self):
        return f'''{super()._str_args()}'''

    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        
        self.name = args[0]
        self.items = [representation_item.parse(a) for a in args[1]]
        self.context = context.parse(args[2])