# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 18:00:51 2022

@author: USER
"""

import numpy as np
import matplotlib.pyplot as plt
#import matplotlib.cm as cm
from matplotlib.colors import LogNorm
#import matplotlib.cbook as cbook

def var(M, N, fm, fn):
    #s = (n0/m0)*(fn/fm)*((1-fm)/(1-fn))
    #root = s**(1/(q+1))
    #cost = 1/(1+root)
    #N = n0*cost**q
    #M = m0*(1-cost)**q
    var = (fm/(fn-1/N))*((fm+1/M)/(fn-2/N)-(fm)/(fn-1/N))
    return var
    

fm = float(input("Enter success ratio of mission M: "))
fn = float(input("Enter success ratio of mission N: "))

M = np.arange(1,1/fm,1)
N = np.arange(1,1/fn,1)



X,Y = np.meshgrid(M, N)
Z = var(X, Y, fm, fn)

print(Z)

#Just testing a sample
#s=minvar(X, Y ,0.99,0.99,m0,n0,q)/abs(Z).max()
#print(s)

Z = Z/(abs(Z).max())
Z = Z[::-1]


fig, ax = plt.subplots()
#ax.set_xscale("log")
#ax.set_yscale("log")
ax.set_xlabel('Sample size - Mission M')
ax.set_ylabel('Sample size - Mission N')
ax.set_title('Dependence of variance on Mission sample size')



pcm = ax.pcolormesh(X, Y, Z,
                   vmin=abs(Z).min(), vmax=abs(Z).max(),
                   cmap='jet_r', shading='nearest')
fig.colorbar(pcm, ax=ax, extend='max')