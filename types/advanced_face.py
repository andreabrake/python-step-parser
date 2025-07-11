from parsers.helpers import get_arguments, clean_display, clean_display_list
from parsers.face_bound import FaceBound
from parsers.abstract_parsers.surface import parse_surface

class AdvancedFace():
    def __init__(self, conn, key: int):
        self.key = key
        self.__get_arguments(conn)
        pass

    def __str__(self):
        return f'''ADVANCED_FACE (
    key          = {self.key}
    name         = {self.name}
    bounds       = {clean_display_list(self.bounds)}
    geometry     = {clean_display(self.geometry)}
    same_sense   = {self.same_sense}
)
'''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        self.name = args[0]
        self.bounds = [FaceBound(conn, b) for b in args[1]]
        self.geometry = parse_surface(conn, args[2])
        self.same_sense = args[3]