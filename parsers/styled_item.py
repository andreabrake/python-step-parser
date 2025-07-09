from parsers.helpers import get_arguments, clean_display, clean_display_list
from parsers.abstract_parsers.item import parse_item
from parsers.presentation_style_assignment import PresentationStyleAssignment

class StyledItem():
    def __init__(self, conn, key: int):
        self.key = key
        self.__get_arguments(conn)
        pass

    def __str__(self):
        return f'''STYLED_ITEM (
    key          = {self.key}
    name         = {self.name}
    styles       = {clean_display_list(self.styles)}
    item         = {clean_display(self.item)}
)
'''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        self.name = args[0]
        self.styles = [PresentationStyleAssignment(conn, e) for e in args[1]]
        self.item = parse_item(conn, args[2])