from .helpers import get_arguments, clean_display, ChildTypeRegister
from .closed_shell import ClosedShell
from . import solid_model

type_name = 'MANIFOLD_SOLID_BREP'
class ManifoldSolidBrep(solid_model.SolidModel):
    type_name = type_name

    def __init__(self, conn, key: int, resolve_children: bool = False):
        super().__init__(conn, key, resolve_children)
        self.__get_arguments(conn)

    def __str__(self):
        return f'''{type_name} (
{self._str_args()}
)
'''

    def _str_args(self):
        return f'''{super()._str_args()}
    outer        =  {clean_display(self.outer) if self.resolve_children else self.outer}'''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        
        if self.resolve_children:
            self.outer = ClosedShell(conn, args[1])
        else:
            self.outer = args[1]

child_type_register = ChildTypeRegister(type_name, solid_model.child_type_register)
child_type_register.register(type_name, lambda conn, key: ManifoldSolidBrep(conn, key))