from step_types.helpers import get_arguments, clean_display, clean_display_list
from step_types.face_bound import FaceBound
from step_types.abstract_types.surface import parse_surface
from step_types.transient import Transient

class AdvancedFace(Transient):
    type_name = 'ADVANCED_FACE'

    def __init__(self, conn, key: int):
        super().__init__(conn, key)
        self.__get_arguments(conn)

    def __str__(self):
        return f'''{self.type_name} (
{self._str_args()}
)
'''

    def _str_args(self):
        return f'''{super()._str_args()}
    name         = {self.name}
    bounds       = {clean_display_list(self.bounds)}
    geometry     = {clean_display(self.geometry)}
    same_sense   = {self.same_sense}'''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        self.name = args[0]
        self.bounds = [FaceBound(conn, b) for b in args[1]]
        self.geometry = parse_surface(conn, args[2])
        self.same_sense = args[3]

    def get_geometry(self):
        return super().get_geometry() | {
            'bounds': [b.get_geometry() for b in self.bounds],
            'surface': self.geometry.get_geometry()
        }