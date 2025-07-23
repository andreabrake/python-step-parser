from .helpers import get_arguments, clean_display, clean_display_list
from .abstract_types import representation_item, context

class ShapeDefinitionRepresentation():
    def __init__(self, conn, key: int):
        self.key = key
        self.__get_arguments(conn)
        pass

    def __str__(self):
        return f'''SHAPE_DEFINITION_REPRESENTATION (
    key          = {self.key}
    name         = {self.name}
    items        = {clean_display_list(self.items)}
    context      = {clean_display(self.context)}
)
'''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        
        self.name = args[0]
        self.items = [representation_item.parse(a) for a in args[1]]
        self.context = context.parse(args[2])