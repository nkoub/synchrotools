#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author      : Nikos E Kouvaris
# Email       : nkouba@gmail.com
# Date        : 01/06/2017
# Update      : 07/05/2018


import numpy as np


def mean_correlation_spacetime(spacetime):
    """Returns the (mean) correlation coefficient for a NxT numpy array.

    Parameters:
    -----------
    spacetime: NxT numpy array (N: Number of nodes, T: Time)
               Each row represents a timeseries of the corresponding node.
    Returns:
    --------
    avgcorr: Mean correlation (scalar number)
    """
    corrmat = np.corrcoef(spacetime)    # Calculate the correlation matrix
    avgcorr = corrmat.mean()            # Take its average value
    return avgcorr
