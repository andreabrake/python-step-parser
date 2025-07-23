from .topological_representation_item import TopologicalRepresentationItem

class Loop(TopologicalRepresentationItem):
    type_name = 'Loop'

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