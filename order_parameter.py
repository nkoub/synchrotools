#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author      : Nikos E Kouvaris
# Email       : nkouba@gmail.com
# Date        : 15/03/2017
# Update      : 07/05/2018


import numpy as np


def global_order_parameter_spacetime_slow(spacetime):
    """Returns the Kuramoto order parameter for an NxT numpy array.

    Parameters:
    -----------
    spacetime: NxT numpy array (N: number of nodes, T: time)
               Each row of represents a timeseries of the corresponding node.

    Returns:
    --------
    r: Global order parameter (Scalar number)
    """
    sum_theta = np.sum(np.exp(0.0 + 1j*spacetime), axis=0)
    r = abs(sum_theta) / (1.0*spacetime.shape[0])
    return r


def global_order_parameter_spacetime(spacetime):
    """Returns the Kuramoto order parameter for an NxT numpy array.

    It is faster than the global_order_parameter_slow

    Parameters:
    -----------
    spacetime: NxT numpy array (N: number of nodes, T: time).
               Each row represents a timeseries of the corresponding node.

    Returns:
    --------
    r: Global order parameter (Scalar number)
    """
    scos = np.cos(spacetime).sum(axis=0)
    ssin = np.sin(spacetime).sum(axis=0)
    r = np.sqrt((scos*scos + ssin*ssin)) / (1.0*spacetime.shape[0])
    return r


def local_order_parameter_space(space, order):
    """Returns the Kuramoto order parameter for an Nx1 numpy array
    within a certain neighborhood.

    Parameters:
    -----------
    space: Nx1 numpy array (N: number of nodes)
           It contains the phases of the N nodes.
    order: Number of neighboring nodes to the left and to the right
           taken into account in the calculation of the order parameter.

    Returns:
    --------
    local_r: Local order parameter (Vector with N entries)
    """
    N = space.shape[0]
    local_r = np.zeros(N)
    list_i = np.array([i for i in range(N)])

    for i in list_i:
        sum_theta = np.exp(0.0 + 1j * np.zeros_like(space))
        j_delta = 0
        list_j = np.array([j for j in range(i-order, i+order)])
        for j in list_j:
            # check the boundaries
            if (j < 0):
                j_delta = j + N
            elif (j > (N-1)):
                j_delta = j - N
            else:
                j_delta = j
            # summarize all the neighbors
            if (i != j):
                sum_theta += np.exp(0.0 + 1j*space[j_delta])
            # take the absolute value
            local_r[i] = (1.0/(2.0*order)) * abs(np.sum(sum_theta, axis=0))
    return local_r


def local_order_parameter_spacetime(spacetime, order):
    """Returns the Kuramoto order parameter for a NxT numpy array
    within a certain neighborhood.

    Parameters:
    -----------
    spacetime: NxT numpy array (N: Number of nodes, T: time)
               Each row represents a timeseries of the corresponding node.
    order: Number of neighboring nodes to the left and to the right
           taken into account in the calculation of the order parameter.

    Returns:
    --------
    local_r: Local order parameter for each time step (NxT numpy array)
    """
    space, time = spacetime.shape
    local_r = np.zeros(space)
    times = np.array([t for t in range(time)])
    local_r = np.zeros_like(spacetime)
    for t in times:
        local_r[:, t] = local_order_parameter_space(spacetime[:, t], order)
    return local_r
