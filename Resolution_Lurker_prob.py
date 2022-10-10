# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 22:16:14 2022

@author: USER
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from scipy.stats import norm
from scipy.stats import expon

# P(N>0|null)
def prob(p, R, f_R, N):
    #cdf = norm.cdf(R, loc = 1.5, scale = 0.09)-norm.cdf(0,1.5,0.09)
    cdf = expon.cdf(R)
    prob_var = p*(cdf+(1-f_R)**N*(1-cdf))/(1-p*(1-(1-f_R)**N)*(1-cdf))
    return prob_var

f_R = float(input("Enter fraction of area measured: "))
#D = float(input("Diameter of NTA: "))
N = float(input("Enter the saturation number of NTAs: "))


p = np.arange(0.01,1.00,0.01)
R = np.arange(0,3,0.01)

X,Y = np.meshgrid(p, R)
Z = prob(X,Y,f_R,N)

Z = Z/(abs(Z).max())
#Z = Z[::-1]
#Z = np.round(Z,2)+10**(-4)

fig, ax = plt.subplots()
#ax.set_xscale("log")
#ax.set_yscale("log")
ax.set_xlabel('Probability of NTAs existing')
ax.set_ylabel('Resolution of detector')
ax.set_title('Variation of optimistic probability')



pcm = ax.pcolormesh(X, Y, Z,
                   vmin=abs(Z).min(), vmax=abs(Z).max(),
                   cmap='jet_r', shading='nearest')
fig.colorbar(pcm, ax=ax, extend='max')
#ax.contourf(X,Y,Z, cmap='RdBu_r')

 