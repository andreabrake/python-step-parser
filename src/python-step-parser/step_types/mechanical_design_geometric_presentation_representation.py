from .helpers import get_complex_or_base_arguments, ChildTypeRegister
from . import presentation_representation

type_name = 'MECHANICAL_DESIGN_GEOMETRIC_PRESENTATION_REPRESENTATION'

class MechanicalDesignGeometricPresentationRepresentation(presentation_representation.PresentationRepresentation):
    type_name = type_name

    def __init__(self, conn, key: int):
        super().__init__(conn, key)
        self.__get_arguments(conn)

    def __str__(self):
        return f'''{self.type_name} (
{self._str_args()}
)
'''
    
    def _str_args(self):
        return f'''{super()._str_args()}'''
    
    def __get_arguments(self, conn):
        pass


presentation_representation.child_type_register.register(type_name, lambda conn, key: MechanicalDesignGeometricPresentationRepresentation(conn, key))