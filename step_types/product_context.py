from .helpers import get_arguments, clean_display
from .application_context import ApplicationContext

class ProductContext():
    def __init__(self, conn, key: int):
        self.key = key
        self.__get_arguments(conn)
        pass

    def __str__(self):
        return f'''PRODUCT_CONTEXT (
    key          = {self.key}
    name         = {self.name}
    discipline   = {self.discipline_type}
    app_context  = {clean_display(self.application_context)}
)
'''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        self.name = args[0]
        self.frame_of_reference = args[1]
        self.discipline_type = args[2]

        self.application_context = self.__get_application_context(conn)

    def __get_application_context(self, conn):
        return ApplicationContext(conn, self.frame_of_reference)