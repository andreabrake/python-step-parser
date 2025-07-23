from .helpers import get_arguments, clean_display, clean_display_list
from .abstract_types import representation_item, context
from .measure_with_unit import MeasureWithUnit

class UncertaintyMeasureWithUnit(MeasureWithUnit):
    def __init__(self, conn, key: int):
        super().__init__(conn, key)
        self.__get_arguments(conn)

    def __str__(self):
        return f'''UNCERTAINTY_MEASURE_WITH_UNIT (
{self._str_args()}
)
'''
    
    def _str_args(self):
        return f'''{super()._str_args()}
    name         = {self.name}
    description  = {self.description}'''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        
        self.name = args[3]
        self.description = args[3]