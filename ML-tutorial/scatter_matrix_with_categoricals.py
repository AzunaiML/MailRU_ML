# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 14:06:30 2016

@author: AzunaiML

data : pandas data frame

col1 : string
    column name in the data variable for X-axis
    
col2 : string
    column name in the data variable for Y-axis
    
categorical_param : string
    name of the categorical param in the data variable 

figsize : tuple of integers, optional, default: (10, 6)
   width, height in inches.

alpha : scalar, optional, default: 0.75
   The alpha blending value, between 0 (transparent) and 1 (opaque)

"""

import matplotlib.pyplot as plt
from itertools import cycle
import matplotlib.cm as cm
import numpy as np

plt.style.use('ggplot')


def scatter_matrix_with_categoricals(data,
                                     col1,
                                     col2,
                                     categorical_param,
                                     figsize=(10, 6),
                                     alpha=0.75):
                                     
    categorials = data[categorical_param].unique()
    colors = cm.rainbow(np.linspace(0,
                                    1,
                                    len(categorials)))

    color_cycle = cycle(colors)

    plt.figure(figsize=figsize)

    for c in categorials:
        plt.scatter(data[col1][data[categorical_param] == c],
                    data[col2][data[categorical_param] == c],
                    alpha=alpha,
                    color=color_cycle.next(),
                    label=c)

    plt.xlabel(col1)
    plt.ylabel(col2)
    plt.legend(loc='best')
    plt.show()
