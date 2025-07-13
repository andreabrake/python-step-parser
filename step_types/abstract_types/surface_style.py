from step_types.helpers import get_entity_type

from step_types.surface_style_fill_area import SurfaceStyleFillArea
from step_types.surface_style_rendering_with_properties import SurfaceStyleRenderingWithProperties

def parse(conn, id: int):
    type = get_entity_type(conn, id)
    # print('parsing surface style', type)
    if type == 'SURFACE_STYLE_FILL_AREA':
        return SurfaceStyleFillArea(conn, id)
    elif type == 'SURFACE_STYLE_RENDERING_WITH_PROPERTIES':
        return SurfaceStyleRenderingWithProperties(conn, id)
    raise Exception(f'Cannot find surface style with type {type}')