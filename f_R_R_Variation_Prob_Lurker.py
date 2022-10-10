# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 22:50:12 2022

@author: USER
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from scipy.stats import norm
from scipy.stats import expon

def prob(f_R, R, p, N):
    cdf = norm.cdf(R, loc=1.5, scale=0.3)
    #cdf = expon.cdf(R, 0, scale=2)
    prob_var = p*(cdf+(1-f_R)**N*(1-cdf))/(1-p*(1-(1-f_R)**N)*(1-cdf))
    #prob_var = (1-p)/(1 - (1-(1-f_R)**N)*(1 - cdf)*p)
    return prob_var

p = float(input("Enter prior existence probability: "))
#D = float(input("Diameter of NTA: "))
N = float(input("Enter the saturation number of NTAs: "))


f_R = np.arange(0.01,1.00,0.01)
R = np.arange(0,3,0.01)

X,Y = np.meshgrid(f_R, R)
Z = prob(X,Y,p,N)

Z = Z/(abs(Z).max())
#Z = Z[::-1]
#Z = np.round(Z,2)+10**(-4)

fig, ax = plt.subplots()
#ax.set_xscale("log")
#ax.set_yscale("log")
ax.set_xlabel('Fraction of area sampled')
ax.set_ylabel('Resolution of detector')
ax.set_title('Variation of optimistic probability')
#ax.set_title('Variation of pessimistic probability')


pcm = ax.pcolormesh(X, Y, Z,
                   vmin=abs(Z).min(), vmax=abs(Z).max(),
                   cmap='jet_r', shading='nearest')
fig.colorbar(pcm, ax=ax, extend='max')
CS = ax.contour(X, Y, Z, cmap='copper')
ax.clabel(CS, inline=True, fontsize=10)