from parsers.helpers import get_entity_type

from parsers.colour_rgb import ColourRGB
from parsers.draughting_pre_defined_colour import DraughtingPreDefinedColour

def parse_colour(conn, id: int):
    type = get_entity_type(conn, id)
    print('parsing colour', type)
    if type == 'DRAUGHTING_PRE_DEFINED_COLOUR':
        return DraughtingPreDefinedColour(conn, id)
    else:
        return ColourRGB(conn, id)