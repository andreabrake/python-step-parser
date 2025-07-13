from step_types.helpers import get_arguments, clean_display, clean_display_list
from step_types.product_definition_usage import ProductDefinitionUsage

class AssemblyComponentUsage(ProductDefinitionUsage):
    def __init__(self, conn, key: int):
        super().__init__(conn, key)
        self.__get_arguments(conn)

    def __str__(self):
        return f'''ASSEMBLY_COMPONENT_USAGE (
{self._str_args()}
)
'''
    
    def __str__(self):
        return f'''{super()._str_args()}
    designator   = {self.reference_designator}'''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        
        self.reference_designator = args[5]