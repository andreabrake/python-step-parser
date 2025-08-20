from .helpers import get_complex_or_base_arguments, clean_display, clean_display_list
from . import representation_item
from .transient import Transient
from .item_defined_transformation import ItemDefinedTransformation


class ShapeRepresentationRelationship(Transient):
    type_name = 'SHAPE_REPRESENTATION_RELATIONSHIP'

    def __init__(self, conn, key: int):
        super().__init__(conn, key)
        self.__get_arguments(conn)

    def __str__(self):
        return f'''SHAPE_REPRESENTATION_RELATIONSHIP (
{self._str_args()}
)
'''
    
    def _str_args(self):
        return f'''{super()._str_args()}
    name         = {self.name}
    description  = {self.description}
    shape_rep_1  = {clean_display(self.shape_representation_1)}
    shape_rep_2  = {clean_display(self.shape_representation_2)}
    transform    = {clean_display(self.transformation)}'''
    
    def __get_arguments(self, conn):
        args = get_complex_or_base_arguments(conn,
                                             self.key,
                                             ['REPRESENTATION_RELATIONSHIP',
                                              'REPRESENTATION_RELATIONSHIP_WITH_TRANSFORMATION',
                                              'SHAPE_REPRESENTATION_RELATIONSHIP'])
        
        self.name = args[0]
        self.description = args[1]
        self.shape_representation_1 = representation_item.child_type_register.parse(conn, args[2])
        self.shape_representation_2 = representation_item.child_type_register.parse(conn, args[3])
        if len(args) > 4:
            self.transformation = ItemDefinedTransformation(conn, args[4])
        else:
            self.transformation = None
