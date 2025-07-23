from .helpers import get_arguments, clean_display, clean_display_list
from .transient import Transient
from .product_definition_shape import ProductDefinitionShape
from .shape_representation_relationship import ShapeRepresentationRelationship

class ContextDependentShapeRepresentation(Transient):
    def __init__(self, conn, key: int):
        super().__init__(conn, key)
        self.__get_arguments(conn)

    def __str__(self):
        return f'''CONTEXT_DEPENDENT_SHAPE_REPRESENTATION (
{self._str_args()}
)
'''
    
    def _str_args(self):
        return f'''{super()._str_args()}
    shape_rep    = {clean_display(self.representation)}
    product      = {clean_display(self.product)}'''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        
        self.representation = ShapeRepresentationRelationship(conn, args[0])
        self.product = ProductDefinitionShape(conn, args[1])