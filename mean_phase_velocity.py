#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author      : Nikos E Kouvaris
# Email       : nkouba@gmail.com
# Date        : 04/04/2017
# Update      : 07/05/2018


import numpy as np
from scipy.signal import argrelextrema


def mean_phase_velocity_spacetime(spacetime, order):
    '''Mean phase velocity for a NxT numpy array.

    Parameters:
    -----------
    spacetime: NxT numpy array (N: Number of nodes, T: Time)
           Each row represents a timeseries of the corresponding node.
    order: Number of neighboring nodes to the left and to the right
           taken into account in the calculation.

    Returns:
    --------
    omega: Mean phase velocity of each node (Nx1 numpy array)
    '''
    M = np.zeros(spacetime.shape[0])
    for i in range(0, spacetime.shape[0]):
        M[i] = len(argrelextrema(spacetime[i], np.greater, order=order)[0])
    omega = (2.0*np.pi*M) / (1.0*spacetime.shape[1])
    return omega
