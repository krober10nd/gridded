#!/usr/bin/env python

from __future__ import (absolute_import, division, print_function, unicode_literals)
__version__ = "0.0.7"

from gridded.gridded import Dataset
from gridded.grids import Grid
from gridded.variable import Variable, VectorVariable

from gridded.depth import S_Depth
S_Depth._default_component_types['variable'] = Variable

__all__ = ["Variable",
           "VectorVariable",
           "Grid"]
