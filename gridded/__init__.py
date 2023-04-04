#!/usr/bin/env python

__version__ = "0.5.3"


VALID_SGRID_LOCATIONS = (None, 'center','edge1','edge2','node')
VALID_UGRID_LOCATIONS = (None, 'node', 'face', 'edge', 'boundary')
VALID_LOCATIONS = set(VALID_SGRID_LOCATIONS + VALID_UGRID_LOCATIONS)


from .gridded import Dataset
from .grids import Grid, Grid_R, Grid_S, Grid_U
from .variable import Variable, VectorVariable
from .time import Time

from .depth import DepthBase
DepthBase._default_component_types['variable'] = Variable



__all__ = ["Variable",
           "VectorVariable",
           "Grid",
           "Grid_R",
           "Grid_S",
           "Grid_U",
           "Dataset",
           "Time"]

