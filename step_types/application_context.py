from .helpers import get_arguments

class ApplicationContext():
    def __init__(self, conn, key: int):
        self.key = key
        self.__get_arguments(conn)
        pass

    def __str__(self):
        return f'''APPLICATION_CONTEXT (
    key          = {self.key}
    name         = {self.name}
)
'''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        self.name = args[0]
