#! /usr/bin/env python
# -*- coding: utf-8 -*-

########################################################################
#
#    synchrotools -- a python package for calculating various order
#                        parameters from data files
#
#    (C) Copyright 2017 by Nikos E. Kouvaris <nkouba@gmail.com>
#
#    synchrotools is free software: you can redistribute it and/or modify 
#    it under the terms of the GNU General Public License as published 
#    by the Free Software Foundation, either version 3 of the License, 
#    or (at your option) any later version.
#
#    synchrotools is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of 
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
#    See the GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License 
#    along with this program. If not, see http://www.gnu.org/licenses/.
########################################################################     
    
"""
synchrotools -- a python package for calculating various order
                    parameters from data files
"""

from __future__ import division, absolute_import

# check for Python verion
import sys
if sys.version_info[:2] < (2, 6):
    raise ImportError("Python version 2.6 or later"
                      "is required for multiNetX (%d.%d detected)." % 
                      sys.version_info[:2])
del sys

__author__ = "Nikos E. Kouvaris <nkouba@gmail.com>"
__copyright__ = "Copyright (C) 2017 by Nikos E. Kouvaris <nkouba@gmail.com>"
__license__ = "GNU GPL"
__version__ = "0.1."

   
# Global and Local Kuramoto order parameter
# import synchrotools.order_parameter
from synchrotools.order_parameter import *

# Correlation Coeficient
# import synchrotools.metastability_index
from synchrotools.mean_correlation import *

# Mean Phase Velocity
# import synchrotools.mean_phase_velocity
from synchrotools.mean_phase_velocity import *

# Local Curvature
# import synchrotools.local_curvature
from synchrotools.local_curvature import *

# Chimera-like index
# import synchrotools.chimera_index
from synchrotools.chimera_index import *

# Metastability index
# import synchrotools.metastability_index
from synchrotools.metastability_index import *
