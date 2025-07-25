from ..helpers import get_entity_type

from ..colour_rgb import ColourRGB
from ..draughting_pre_defined_colour import DraughtingPreDefinedColour

def parse(conn, id: int):
    type = get_entity_type(conn, id)
    # print('parsing colour', type)
    if type == 'DRAUGHTING_PRE_DEFINED_COLOUR':
        return DraughtingPreDefinedColour(conn, id)
    elif type == 'COLOUR_RGB':
        return ColourRGB(conn, id)
    # TODO: POLY_LOOP
    raise Exception(f'Cannot find context with type {type}')
