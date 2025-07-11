from parsers.helpers import get_arguments, clean_display_list
from parsers.styled_item import StyledItem

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
)
'''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        self.name = args[0]
        self.styled_items = [StyledItem(conn, e) for e in args[1]]