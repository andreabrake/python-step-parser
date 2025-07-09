from parsers.helpers import get_arguments, clean_display
from parsers.axis2_placement3d import Axis2Placement3d

class ItemDefinedTransformation():
    def __init__(self, conn, key: int):
        self.key = key
        self.__get_arguments(conn)
        pass

    def __str__(self):
        return f'''ITEM_DEFINED_TRANSFORMATION (
    key          = {self.key}
    name         = {self.name}
    description  = {self.description}
    trans_item1  = {clean_display(self.trans_item1)}
    trans_item2  = {clean_display(self.trans_item2)}
)
'''
    
    def __get_arguments(self, conn):
        args = get_arguments(conn, self.key)
        self.name = args[0]
        self.description = args[1]
        self.trans_item1 = Axis2Placement3d(conn, args[2])
        self.trans_item2 = Axis2Placement3d(conn, args[3])