from ..helpers import get_entity_type

from ..surface_style_fill_area import SurfaceStyleFillArea
from ..surface_style_rendering_with_properties import SurfaceStyleRenderingWithProperties

def parse(parser, id: int):
    type = get_entity_type(parser, id)
    # print('parsing surface style', type)
    if type == 'SURFACE_STYLE_FILL_AREA':
        return SurfaceStyleFillArea(parser, id)
    elif type == 'SURFACE_STYLE_RENDERING_WITH_PROPERTIES':
        return SurfaceStyleRenderingWithProperties(parser, id)
    raise Exception(f'Cannot find surface style with type {type}')