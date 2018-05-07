#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author      : Nikos E Kouvaris
# Email       : nkouba@gmail.com
# Date        : 15/03/2017
# Update      : 04/04/2017


import numpy as np



def global_order_parameter_spacetime_slow(spacetime):
    """Returns the Kuramoto order parameter for a NxT numpy array.

    Parameters:
    -----------
    spacetime: Is a NxT numpy array 
               N is the number of the nodes and T is the total time.
               Each row represents a timeseries of the corresponding node.
    Returns:
    --------
    r: a scalar number
    """
    sum_theta = np.sum(np.exp(0.0 + 1j * spacetime), axis=0)
    r = abs(sum_theta) / (1.0*spacetime.shape[0])
    return r



def global_order_parameter_spacetime(spacetime):
    """Returns the Kuramoto order parameter for a NxT numpy array.

    It is faster than the global_order_parameter_slow

    Parameters:
    -----------
    spacetime: Is a NxT numpy array 
               N is the number of the nodes and T is the total time.
               Each row represents a timeseries of the corresponding node.
    Returns:
    --------
    r: a scalar number
    """
    scos = np.cos(spacetime).sum(axis=0)
    ssin = np.sin(spacetime).sum(axis=0)
    r = np.sqrt((scos * scos + ssin * ssin)) / (1.0*spacetime.shape[0])
    return r

 

def local_order_parameter_space(space, order):
    """Returns the Kuramoto order parameter for a Nx1 numpy array 
    within a certain neighborhood.
    
    Parameters:
    -----------
    space: Is Nx1 numpy array. 
           N is the number of the nodes.
           It contains the phases of the N nodes.
    order: the number of neighboring nodes to the left and to the right
           taken into account in the calculation of the order parameter.
    
    Returns:
    --------
    local_r: a vector with N entries that correspond to the 
             local order parameter
    """
    N = space.shape[0]
    local_r = np.zeros(N)
    list_i = np.array([i for i in range(N)])    
    
    for i in list_i:
        sum_theta = np.exp(0.0 + 1j * np.zeros_like(space))
        j_delta = 0
        list_j = np.array([j for j in range(i-order,i+order)])
        
        for j in list_j:            
            # check the boundaries
            if (j<0):
                j_delta = j + N
            elif (j>(N-1)):
                j_delta = j - N
            else:
                j_delta = j
            
            # summarize all the neighbors
            if (i!=j):
            	sum_theta += np.exp(0.0 + 1j * space[j_delta])

            # take the absolute value
            local_r[i] = (1.0/(2.0*order)) * abs(np.sum(sum_theta,axis=0))
    return local_r




def local_order_parameter_spacetime(spacetime, order):
    """Returns the Kuramoto order parameter for a NxT numpy array 
    within a certain neighborhood.
    
    Parameters:
    -----------
    spacetime: Is a NxT numpy array 
               N is the number of the nodes and T is the total time.
               Each row represents a timeseries of the corresponding node.
    order: the number of neighboring nodes to the left and to the right
           taken into account in the calculation of the order parameter.
    
    Returns:
    --------
    local_r: a NxT numpy array that contains the local order parameter for
             each time step
    """
    space, time = spacetime.shape
    local_r = np.zeros(space)
    times = np.array([t for t in range(time)])
    local_r = np.zeros_like(spacetime)
    for t in times:
        local_r[:,t] = local_order_parameter_space(spacetime[:,t],order)
    return local_r     
 

