from .helpers import get_complex_or_base_arguments
from .representation_context import RepresentationContext

class GeometricRepresentationContext(RepresentationContext):
    def __init__(self, conn, key: int):
        super().__init__(conn, key)
        self.__get_arguments(conn)

    def __str__(self):
        return f'''GEOMETRIC_REPRESENTATION_CONTEXT (
{self._str_args()}
)
'''
    
    def _str_args(self):
        return f'''{super()._str_args()}
    dimension    = {self.dimension}'''
    
    def __get_arguments(self, conn):
        args = get_complex_or_base_arguments(conn,
                                             self.key,
                                             ['REPRESENTATION_CONTEXT',
                                              'GEOMETRIC_REPRESENTATION_CONTEXT'])
        
        self.dimension = args[2]
