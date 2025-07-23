from step_types.helpers import get_arguments, clean_display, clean_display_list
from step_types.abstract_types import representation_item
from step_types.shape_representation import ShapeRepresentation

class AdvancedBrepShapeRepresentation(ShapeRepresentation):
    type_name = 'ADVANCED_BREP_SHAPE_REPRESENTATION'

    def __init__(self, conn, key: int):
        super().__init__(conn, key)
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