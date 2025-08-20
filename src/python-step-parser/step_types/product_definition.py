from .helpers import get_arguments, clean_display, ChildTypeRegister
from . import transient
from . import abstract_types
from . import product_definition_formation

type_name = 'PRODUCT_DEFINITION'
class ProductDefinition(transient.Transient):
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
    id           = {self.id}
    description  = {self.description}
    formation    = {clean_display(self.formation)}
    context      = {clean_display(self.context)}'''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        
        self.id = args[0]
        self.description = args[1]
        self.formation = product_definition_formation.child_type_register.parse(conn, args[2])
        self.context = args[3]

child_type_register = ChildTypeRegister(type_name, [
    transient.child_type_register,
    abstract_types.characterized_definition_register
])
child_type_register.register(type_name, lambda conn, key: ProductDefinition(conn, key))