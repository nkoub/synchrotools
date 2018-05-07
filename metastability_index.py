#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author      : Nikos E Kouvaris
# Email       : nkouba@gmail.com
# Date        : 15/03/2017
# Update      : 01/06/2017


import numpy as np
from order_parameter import global_order_parameter_spacetime as gopst



def metastability_index(spacetime, membership):
    """Metastability index.
    spacetime: NxT numpy array where N is the number of the nodes 
            and T is the total time. Each row represents a timeseries 
            of the corresponding node.
    membership: 1xN numpy array with the indices of the communities, 
                e.g. [0,0,3,2,0,1,2,1,0,0,3]
    """

    # Find the unique elements of membership. 
    # They are the indices of the communities
    community_index = np.unique(membership)


    # dictionary for the index of the nodes in each community 
    # keys  : the community index	
    # values: the index of the nodes
    partition = {}
    for m in community_index:
        partition[m] = list(np.argwhere(np.array(membership)==m).flatten()) 


    # dictionary for the order parameters of each community 
    # keys  : the community index	
    # values: the order parameters    
    order_parameter = {}
    for m in community_index:
        order_parameter[m] = gopst(spacetime[partition[m]])


    # dictionary for the (metastability) variance of the order_parameter 
    # in each community 
    # keys  : the community index	
    # values: the metastability index, i.e. the variance of the order parameters    
    sigma_metastable = {}
    for m in community_index:
        sigma_metastable[m] = np.var(order_parameter[m])
        # sigma_metastable[m] = np.sum((order_parameter[m] - 
        #                               np.mean(order_parameter[m])
        #                               )**2
        #                              ) / (len(order_parameter[m])-1)

    
    # The metastability index is the mean of the sigma_metastable 
    # over all communities
    return np.mean(sigma_metastable.values())
