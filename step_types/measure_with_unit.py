from .helpers import get_arguments, clean_display, clean_display_list
from .abstract_types import unit
from .transient import Transient

class MeasureWithUnit(Transient):
    def __init__(self, conn, key: int):
        super().__init__(conn, key)
        self.__get_arguments(conn)

    def __str__(self):
        return f'''MEASURE_WITH_UNIT (
{self._str_args()}
)
'''
    
    def _str_args(self):
        return f'''{super()._str_args()}
    value        = {self.value}
    unit         = {clean_display(self.context)}'''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        
        self.value = args[0]
        self.unit = unit.parse(conn, args[1])