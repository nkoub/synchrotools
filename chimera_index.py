#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author      : Nikos E Kouvaris
# Email       : nkouba@gmail.com
# Date        : 15/03/2017
# Update      : 07/05/2018


import numpy as np
from synchrotools import global_order_parameter_spacetime as gops


def chimera_index(spacetime, membership):
    """Chimera-like index.
    spacetime: NxT numpy array (N: Number of the nodes , T: Time).
               Each row represents a timeseries of the corresponding node.
    membership: 1xN numpy array with the indices of the communities,
                e.g. [0,0,3,3,3,3,2,0,0,2,0,1,2,1,2,2,3]
    Nodes in spacetime and membership must have the same ordering

    Returns:
    --------
    chimera_val: Chimera-like index (scalar value)
    """
    # Find the unique elements of membership. They are the communities indices
    community_index = np.unique(membership)

    # dictionary for the index of the nodes in each community
    # keys  : the community index
    # values: the index of the nodes
    partition = {}
    for m in community_index:
        partition[m] = list(np.argwhere(np.array(membership) == m).flatten())

    # dictionary for the order parameters of each community
    # keys  : the community index
    # values: the order parameters
    order_parameter = {}
    for m in community_index:
        order_parameter[m] = gops(spacetime[partition[m]])

    # dictionary for the mean (over communities) order parameters
    # for each time step
    # keys  : the time snapshots
    # values: the mean order parameters
    mean_order_parameter = {}
    for t in range(len(order_parameter[0])):
        # mean over communities for each time step t
        mean_over_communities = 0.0
        for m in community_index:
            mean_over_communities += order_parameter[m][t]
        mean_order_parameter[t] = mean_over_communities / len(community_index)

    # dictionary for the (chimera-like) variance at each time step t
    # keys  : the community index
    # values: the chimera-like index
    sigma_chimera = {}
    for t in range(len(order_parameter[0])):
        for m in community_index:
            tmp = (order_parameter[m][t] - mean_order_parameter[t])**2
        sigma_chimera[t] = tmp / len(community_index)

    # The chimera index is the mean of the sigma_chimera over all communities
    chimera_val = np.mean(sigma_chimera.values())
    return chimera_val
