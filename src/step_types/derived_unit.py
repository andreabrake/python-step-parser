from .helpers import get_arguments, clean_display_list
from . import transient
from . import derived_unit_element
from .abstract_types import unit_register

type_name = 'DERIVED_UNIT'
class DerivedUnit(transient.Transient):
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
    elements     = {clean_display_list(self.elements)}'''

    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        self.elements = [derived_unit_element.DerivedUnitElement(conn, arg) for arg in args[0]]

transient.child_type_register.register(type_name, lambda conn, key: DerivedUnit(conn, key))
unit_register.register(type_name, lambda conn, key: DerivedUnit(conn, key))