from ..helpers import get_entity_type

from ..colour_rgb import ColourRGB
from ..draughting_pre_defined_colour import DraughtingPreDefinedColour

def parse(parser, id: int):
    type = get_entity_type(parser, id)
    # print('parsing colour', type)
    if type == 'DRAUGHTING_PRE_DEFINED_COLOUR':
        return DraughtingPreDefinedColour(parser, id)
    elif type == 'COLOUR_RGB':
        return ColourRGB(parser, id)
    # TODO: POLY_LOOP
    raise Exception(f'Cannot find context with type {type}')
