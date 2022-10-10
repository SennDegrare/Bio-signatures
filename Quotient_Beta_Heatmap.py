# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 08:22:05 2022

@author: USER
"""

import numpy as np
import matplotlib.pyplot as plt
#import matplotlib.cm as cm
from matplotlib.colors import LogNorm
#import matplotlib.cbook as cbook

def minvar(fm, fn, m0, n0, q):
    s = (n0/m0)*(fn/fm)*((1-fm)/(1-fn))
    root = s**(1/(q+1))
    cost = 1/(1+root)
    N = n0*cost**q
    M = m0*(1-cost)**q
    min_var = (fm/(fn-1/N))*((fm+1/M)/(fn-2/N)-(fm)/(fn-1/N))
    return min_var
    

m0 = float(input("Enter root yield for Mission M: "))
n0 = float(input("Enter root yield for Mission N: "))
q = float(input("Enter order/index of cost growth: "))

fm = np.arange(0.01,1.00,0.005)
fn = np.arange(0.01,1.00,0.005)


X,Y = np.meshgrid(fm, fn)
Z = minvar(X,Y,m0,n0, q)

#Just testing a sample
#s=minvar(0.99,0.99,m0,n0,q)/abs(Z).max()
#print(s)

Z = Z/(abs(Z).max())
Z = Z[::-1]
#Z = np.round(Z,2)+10**(-4)

fig, ax = plt.subplots()
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlabel('Observed fraction - Mission M')
ax.set_ylabel('Observed fraction - Mission N')
ax.set_title('Variation of minimum variance')



pcm = ax.pcolormesh(X, Y, Z,
                   norm = LogNorm(vmin=abs(Z).min(), vmax=abs(Z).max()),
                   cmap='jet_r', shading='nearest')
fig.colorbar(pcm, ax=ax, extend='max')








