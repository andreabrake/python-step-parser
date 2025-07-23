from .helpers import get_complex_or_base_arguments, clean_display_list
from .representation_context import RepresentationContext
from .abstract_types import unit


class GlobalUncertaintyAssignedContext(RepresentationContext):
    def __init__(self, conn, key: int):
        super().__init__(conn, key)
        self.__get_arguments(conn)

    def __str__(self):
        return f'''GLOBAL_UNCERTAINTY_ASSIGNED_CONTEXT (
{self._str_args()}
)
'''
    
    def _str_args(self):
        return f'''{super()._str_args()}
    units        = {clean_display_list(self.units)}'''
    
    def __get_arguments(self, conn):
        args = get_complex_or_base_arguments(conn,
                                             self.key,
                                             ['REPRESENTATION_CONTEXT',
                                              'GLOBAL_UNIT_ASSIGNED_CONTEXT'])
        
        self.units = [unit.parse(conn, a) for a in args[2]]
