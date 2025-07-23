from step_types.helpers import get_arguments, clean_display, clean_display_list
from step_types.assembly_component_usage import AssemblyComponentUsage 

class NextAssemblyUsageOccurrence(AssemblyComponentUsage):
    def __init__(self, conn, key: int):
        super().__init__(conn, key)
        self.__get_arguments(conn)

    def __str__(self):
        return f'''NEXT_ASSEMBLY_USAGE_OCCURRENCE (
{self._str_args()}
)
'''
    
    def _str_args(self):
        return f'{super()._str_args()}'
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        
        # No additional args