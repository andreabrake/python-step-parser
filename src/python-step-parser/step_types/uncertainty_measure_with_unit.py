from .helpers import get_arguments
from . import measure_with_unit

type_name = 'UNCERTAINTY_MEASURE_WITH_UNIT'
class UncertaintyMeasureWithUnit(measure_with_unit.MeasureWithUnit):
    def __init__(self, conn, key: int):
        super().__init__(conn, key)
        self.__get_arguments(conn)

    def __str__(self):
        return f'''{type_name} (
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


measure_with_unit.child_type_register.register(type_name, lambda conn, key: UncertaintyMeasureWithUnit(conn, key))