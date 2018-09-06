#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author      : Nikos E Kouvaris
# Email       : nkouba@gmail.com
# Date        : 04/04/2017
# Update      : 05/04/2017


import numpy as np



def local_curvature_space(space, order):
    """Returns the Local Curvature for a Nx1 numpy array.
        
    Parameters:
    -----------
    space: Is Nx1 numpy array. 
           N is the number of the nodes.
           It contains the phases of the N nodes.
    order: the number of neighboring nodes to the left and to the right
           taken into account in the calculation of the local curvature.
    
    Returns:
    --------
    local_curv: a vector with N entries that correspond to the absolute
                value of the local curvature.
    """
    N = space.shape[0]
    local_curv = np.zeros(N)
    list_i = np.array([i for i in range(N)])    
    
    for i in list_i:
        sum_lc = 0.0
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

            # local difference
            lc = space[j_delta] - space[i]
            
            # summarize all the neighbors (Laplacian operator)
            if (i!=j):
                sum_lc += lc

        # take the absolute value, i.e. the local curvature
        local_curv[i] = abs(sum_lc)
    return local_curv                  



def local_curvature_spacetime(spacetime, order):
    """Returns the local curvature for a NxT numpy array. 
    
    Parameters:
    -----------
    spacetime: Is a NxT numpy array. 
               N is the number of the nodes and T is the total time.
               Each row represents a timeseries of the corresponding node.
    order: the number of neighboring nodes to the left and to the right
           taken into account in the calculation of the local curvature.
    
    Returns:
    --------
    local_curv: a NxT numpy array that contains the absolute value 
                of the local curvature at each time step.
    """
    space, time = spacetime.shape
    local_curv = np.zeros(space)
    times = np.array([t for t in range(time)])
    local_curv = np.zeros_like(spacetime)
    for t in times:
        local_curv[:,t] = local_curvature_space(spacetime[:,t],order)
    return local_curv     



def spatial_coherence_index(local_curvature_space, bins, delta):
    """Returns the spatial cohernce index.
    Parameters:
    -----------
    local_curvature_spacetime: Is a NxT numpy array. 
                    N is the number of the nodes and T is the total time.
                    Each column represents the local curvature of the 
                    corresponding time snapshot.
    bins: int or sequence of scalars or str, optional (see np.histogram)
    delta: float

    Returns:
    --------
    g0: a float number between 0 and 1.
    """
    counts, bin_edges = np.histogram(local_curvature_space,
                                bins=bins,
                                range=(np.min(local_curvature_space),
                                       np.max(local_curvature_space)),
                                density=True)
    # cum_counts = np.cumsum(counts)
    bin_widths = np.diff(bin_edges)

    g0 = 0 
    for i in range(len(counts)):
        if bin_edges[i] < delta:
            g0 += counts[i] * bin_widths[i] 
    
    return g0





def local_curvature_network(space, adj):
    """Returns the Local Curvature for a Nx1 numpy array.
       
    Parameters:
    -----------
    space: Is Nx1 numpy array. 
           N is the number of the nodes.
           It contains the phases of the N nodes.
    adj: the adjacency matrix of the network
   
    Returns:
    --------
    local_curv: a vector with N entries that correspond to the absolute
                value of the local curvature.
    """
    N = space.shape[0]
    local_curv = np.zeros(N)
    list_i = np.array([i for i in range(0,N)])    
    list_j = list_i.copy()    

    for i in list_i:
        sum_lc = 0.0
        for j in list_j:     
            if (adj[i,j] == 1.0):
                lc = space[j] - space[i]
                sum_lc += lc

        # take the absolute value, i.e. the local curvature
        local_curv[i] = abs(sum_lc)
    return local_curv  



def local_curvature_network_time(spacetime, adj):
    """Returns the local curvature for a NxT numpy array.
    Parameters:
    -----------
    spacetime: Is a NxT numpy array. 
            N is the number of the nodes and T is the total time.
            Each row represents a timeseries of the corresponding node.
    adj: the adjacency matrix of the network

    Returns:
    --------
    local_curv: a NxT numpy array that contains the absolute 
                value of the local curvature at each time step.
    """
    space, time = spacetime.shape
    local_curv = np.zeros(space)
    times = np.array([t for t in range(time)])
    local_curv = np.zeros_like(spacetime)
    for t in times:
        local_curv[:,t] = local_curvature_network(spacetime[:,t],adj)
    return local_curv  

  
