from .helpers import get_complex_or_base_arguments
from .representation_context import RepresentationContext

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
    uncertainty  = {self.uncertainty}'''
    
    def __get_arguments(self, conn):
        args = get_complex_or_base_arguments(conn,
                                             self.key,
                                             ['REPRESENTATION_CONTEXT',
                                              'GEOMETRIC_REGLOBAL_UNCERTAINTY_ASSIGNED_CONTEXTPRESENTATION_CONTEXT'])
        
        self.uncertainty = args[2]
