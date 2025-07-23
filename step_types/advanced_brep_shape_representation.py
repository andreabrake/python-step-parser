from .helpers import get_arguments, clean_display, clean_display_list
from .abstract_types import representation_item
from .shape_representation import ShapeRepresentation

class AdvancedBrepShapeRepresentation(ShapeRepresentation):
    type_name = 'ADVANCED_BREP_SHAPE_REPRESENTATION'

    def __init__(self, conn, key: int, resolve_children: bool = True):
        super().__init__(conn, key, resolve_children)
        self.__get_arguments(conn)

    def __str__(self):
        return f'''{self.type_name} (
{self._str_args()}
)
'''
    
    def _str_args(self):
        return f'''{super()._str_args()}'''

    
    def __get_arguments(self, conn):
        # No special args
        pass

representation_item.register('ADVANCED_BREP_SHAPE_REPRESENTATION', lambda conn, key: AdvancedBrepShapeRepresentation(conn, key))