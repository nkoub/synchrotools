#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author      : Nikos E Kouvaris
# Email       : nkouba@gmail.com
# Date        : 15/03/2017
# Update      : 07/05/2018


import numpy as np
from order_parameter import global_order_parameter_spacetime as gopst


def metastability_index(spacetime, membership):
    """Metastability index.
    Parameters:
    -----------
    spacetime: NxT numpy array (N: Number of the nodes , T: Time).
               Each row represents a timeseries of the corresponding node.
    membership: 1xN numpy array with the indices of the communities,
                e.g. [0,0,3,3,3,3,2,0,0,2,0,1,2,1,2,2,3]
    Nodes in spacetime and membership must have the same ordering

    Returns:
    --------
    metastability_val: Metastabiity index (scalar value)
    """
    # Find the unique elements of membership.
    # They are the indices of the communities.
    community_index = np.unique(membership)

    # dictionary for the index of the nodes in each community
    # keys  : Community index
    # values: Index of the nodes
    partition = {}
    for m in community_index:
        partition[m] = list(np.argwhere(np.array(membership) == m).flatten())

    # dictionary for the order parameters of each community
    # keys  : Community index
    # values: Order parameters
    order_parameter = {}
    for m in community_index:
        order_parameter[m] = gopst(spacetime[partition[m]])

    # dictionary for the (metastability) variance of the order_parameter
    # in each community
    # keys  : Community index
    # values: Metastability index, i.e. the variance of the order parameters
    sigma_metastable = {}
    for m in community_index:
        sigma_metastable[m] = np.var(order_parameter[m])
        # sigma_metastable[m] = np.sum((order_parameter[m] -
        #                               np.mean(order_parameter[m])
        #                               )**2
        #                              ) / (len(order_parameter[m])-1)

    # The metastability index is the mean of the sigma_metastable
    # over all communities
    metastability_val = np.mean(sigma_metastable.values())
    return metastability_val
