from step_types.helpers import get_entity_type

from step_types.conical_surface import ConicalSurface
from step_types.cylindrical_surface import CylindricalSurface
from step_types.degenerate_toroidal_surface import DegenerateToroidalSurface
from step_types.plane import Plane
from step_types.spherical_surface import SphericalSurface
from step_types.toroidal_surface import ToroidalSurface

def parse_surface(conn, id: int):
    type = get_entity_type(conn, id)
    print('parsing surface', type)
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
    else:
        return Plane(conn, id)
