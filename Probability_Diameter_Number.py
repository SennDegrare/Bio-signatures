# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 23:09:12 2022

@author: USER
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from scipy.stats import norm

def prob_det(N, D, f_R):
    cdf = norm.cdf(D)
    prob_var = (1-(1-f_R)**N)*cdf
    return prob_var

f_R = float(input("Enter fraction of area measured: "))
#D = float(input("Diameter of NTA: "))
#N = float(input("Enter the saturation number of NTAs: "))


N = np.arange(1,10,1)
D = np.arange(0,5,0.01)

#X,Y = np.meshgrid(N, D)
Z = prob_det(N,D,f_R)

Z = Z/(abs(Z).max())
#Z = Z[::-1]


fig, ax = plt.subplots()
#ax.set_xscale("log")
#ax.set_yscale("log")
ax.set_xlabel('Number of NTAs existing assumed')
ax.set_ylabel('Diameter of NTAs')
ax.set_title('Variation of probability of detection')



#pcm = ax.pcolormesh(X, Y, Z,
                   #norm = LogNorm(vmin=abs(Z).min(), vmax=abs(Z).max()),
                   #cmap='jet_r', shading='nearest')
#fig.colorbar(pcm, ax=ax, extend='max')

print(Z)

 
