from ..helpers import get_entity_type, get_complex_items

from ..conical_surface import ConicalSurface
from ..cylindrical_surface import CylindricalSurface
from ..degenerate_toroidal_surface import DegenerateToroidalSurface
from ..plane import Plane
from ..spherical_surface import SphericalSurface
from ..toroidal_surface import ToroidalSurface
from ..b_spline_surface_with_knots import BSplineSurfaceWithKnots

from ..surface import Surface

def parse_surface(parser, id: int) -> Surface:
    type = get_entity_type(parser, id)
    # print('parsing surface', type)
    if type == 'CONICAL_SURFACE':
        return ConicalSurface(parser, id)
    elif type == 'CYLINDRICAL_SURFACE':
        return CylindricalSurface(parser, id)
    elif type == 'DEGENERATE_TOROIDAL_SURFACE':
        return DegenerateToroidalSurface(parser, id)
    elif type == 'SPHERICAL_SURFACE':
        return SphericalSurface(parser, id)
    elif type == 'TOROIDAL_SURFACE':
        return ToroidalSurface(parser, id)
    elif type == 'PLANE':
        return Plane(parser, id)
    elif type == 'B_SPLINE_SURFACE_WITH_KNOTS':
        return BSplineSurfaceWithKnots(parser, id)
    elif type == 'COMPLEX':
        complex_items = get_complex_items(parser, id)
        complex_item_types = [i.type for i in complex_items]
        raise Exception(f'Cannot find context with type {type} [{','.join(complex_item_types)}]')
    raise Exception(f'Cannot find context with type {type}')