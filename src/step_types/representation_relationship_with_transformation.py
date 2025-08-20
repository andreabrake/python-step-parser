from .helpers import get_complex_or_base_arguments

class RepresentationRelationship():
    def __init__(self, conn, key: int):
        self.key = key
        self.__get_arguments(conn)
        pass

    def __str__(self):
        return f'''REPRESENTATION_RELATIONSHIP_WITH_TRANSFORMATION (
    key          = {self.key}
    name         = {self.name}
    description  = {self.description}
    rep_1        = {self.representation_1}
    rep_2        = {self.representation_2}
    transform    = {self.transformation}
)
'''
    
    def __get_arguments(self, conn):
        args = get_complex_or_base_arguments(conn,
                                             self.key,
                                             ['REPRESENTATION_RELATIONSHIP',
                                              'REPRESENTATION_RELATIONSHIP_WITH_TRANSFORMATION'])
        
        self.name = args[0]
        self.description = args[1]
        self.representation_1 = args[2]
        self.representation_2 = args[3]
        self.transformation = args[4]