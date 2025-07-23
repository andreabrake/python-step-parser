from .helpers import get_complex_or_base_arguments
from .transient import Transient

class RepresentationContext(Transient):
    def __init__(self, conn, key: int):
        super().__init__(conn, key)
        self.__get_arguments(conn)

    def __str__(self):
        return f'''REPRESENTATION_CONTEXT (
{self._str_args()}
)
'''
    
    def _str_args(self):
        return f'''{super()._str_args()}
    context_id   = {self.context_identifier}
    context_type = {self.context_type}'''

    def __get_arguments(self, conn):
        args = get_complex_or_base_arguments(conn,
                                             self.key,
                                             ['REPRESENTATION_CONTEXT',])
        
        self.context_identifier = args[0]
        self.context_type = args[1]
