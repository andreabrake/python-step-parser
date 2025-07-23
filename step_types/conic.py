from step_types.helpers import get_arguments, clean_display
from step_types.axis2_placement3d import Axis2Placement3d
from step_types.curve import Curve

class Conic(Curve):
    type_name = 'CONIC'

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
    position     = {clean_display(self.position)}'''

    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        self.position = Axis2Placement3d(conn, args[1])