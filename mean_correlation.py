#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author      : Nikos E Kouvaris
# Email       : nkouba@gmail.com
# Date        : 01/06/2017
# Update      : 01/06/2017


import numpy as np





def mean_correlation_spacetime(spacetime):
    """Returns the (mean) correlation coefficient for a NxT numpy array.


    Parameters:
    -----------
    spacetime: Is a NxT numpy array 
               N is the number of the nodes and T is the total time.
               Each row represents a timeseries of the corresponding node.
    Returns:
    --------
    avgcorr: a scalar number
    """    
    corrmat = np.corrcoef(spacetime)    # Calculate the correlation matric 
    avgcorr = corrmat.mean()            # Take its average value
    
    return avgcorr

 
