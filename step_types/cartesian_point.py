from step_types.helpers import get_arguments

class CartesianPoint():
    def __init__(self, conn, key: int):
        self.key = key
        self.__get_arguments(conn)
        pass

    def __str__(self):
        return f'''CARTESIAN_POINT (
    key          = {self.key}
    name         = {self.name}
    coordinates  = {self.coordinates}
)
'''
    
    def __get_arguments(self, conn):
        print(f'getting cartesian point {self.key}')
        args = get_arguments(conn, self.key)
        self.name = args[0]
        self.coordinates = args[1]