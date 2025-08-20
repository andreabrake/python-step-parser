from .helpers import get_complex_or_base_arguments, ChildTypeRegister
from . import representation_context

type_name = 'GEOMETRIC_REPRESENTATION_CONTEXT'
class GeometricRepresentationContext(representation_context.RepresentationContext):
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
    dimension    = {self.dimension}'''
    
    def __get_arguments(self, conn):
        args = get_complex_or_base_arguments(conn,
                                             self.key,
                                             ['REPRESENTATION_CONTEXT',
                                              'GEOMETRIC_REPRESENTATION_CONTEXT'])
        
        self.dimension = args[2]

child_type_register = ChildTypeRegister(type_name, representation_context.child_type_register)
child_type_register.register(type_name, lambda conn, key: GeometricRepresentationContext(conn, key))