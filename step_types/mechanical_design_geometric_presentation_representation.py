from step_types.helpers import get_arguments, clean_display_list, clean_display
from step_types.styled_item import StyledItem
from step_types.geometric_representation_context import GeometricRepresentationContext

class MechanicalDesignGeometricPresentationRepresentation():
    def __init__(self, conn, key: int):
        self.key = key
        self.__get_arguments(conn)
        pass

    def __str__(self):
        return f'''MECHANICAL_DESIGN_GEOMETRIC_PRESENTATION_REPRESENTATION (
    key          = {self.key}
    name         = {self.name}
    styled_items = {clean_display_list(self.styled_items)}
    context      = {clean_display(self.context)}
)
'''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        self.name = args[0]
        self.styled_items = [StyledItem(conn, e) for e in args[1]]
        self.context = GeometricRepresentationContext(conn, args[2])