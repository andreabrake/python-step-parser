from step_types.helpers import get_entity_type, get_complex_items

from step_types.conical_surface import ConicalSurface
from step_types.cylindrical_surface import CylindricalSurface
from step_types.degenerate_toroidal_surface import DegenerateToroidalSurface
from step_types.plane import Plane
from step_types.spherical_surface import SphericalSurface
from step_types.toroidal_surface import ToroidalSurface
from step_types.b_spline_surface_with_knots import BSplineSurfaceWithKnots

from step_types.surface import Surface

def parse_surface(conn, id: int) -> Surface:
    type = get_entity_type(conn, id)
    # print('parsing surface', type)
    if type == 'CONICAL_SURFACE':
        return ConicalSurface(conn, id)
    elif type == 'CYLINDRICAL_SURFACE':
        return CylindricalSurface(conn, id)
    elif type == 'DEGENERATE_TOROIDAL_SURFACE':
        return DegenerateToroidalSurface(conn, id)
    elif type == 'SPHERICAL_SURFACE':
        return SphericalSurface(conn, id)
    elif type == 'TOROIDAL_SURFACE':
        return ToroidalSurface(conn, id)
    elif type == 'PLANE':
        return Plane(conn, id)
    elif type == 'B_SPLINE_SURFACE_WITH_KNOTS':
        return BSplineSurfaceWithKnots(conn, id)
    elif type == 'COMPLEX':
        complex_items = get_complex_items(conn, id)
        complex_item_types = [i.type for i in complex_items]
        raise Exception(f'Cannot find context with type {type} [{','.join(complex_item_types)}]')
    raise Exception(f'Cannot find context with type {type}')