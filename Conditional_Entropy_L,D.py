# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 00:04:41 2022

@author: USER
"""

#Conditional Entropy of L|D


import matplotlib.pyplot as plt
import numpy as np


def x(FP,FN):
    return FP/(1-FN)

def Lambda(FP,FN):
    return (1-FP)/FN

def Pplus(x):
    temp = (1-x+x*np.log(x))/(1-x)**2
    return temp
    
def Pminus(Ld):
    temp = 1 - (1-Ld+Ld*np.log(Ld))/(1-Ld)**2
    return temp
    
def Cond_Entro(Pplus,Pminus,p):
    tempplus = Pplus*np.log(Pplus)*p + (1-Pplus)*np.log(1-Pplus)*p
    tempminus = Pminus*np.log(Pminus)*(1-p) + (1-Pminus)*np.log(1-Pminus)*(1-p)
    Cond_Entro = -1*(tempplus + tempminus)
    return Cond_Entro

FP = np.arange(0.01, 0.99, 0.01)
FN = np.arange(0.01, 0.99, 0.01)

X,Y = np.meshgrid(FP,FN)

parr = np.arange(0.0,1.1,0.1)


for p in parr:
    x_ = x(X,Y)
    LD = Lambda(X,Y)
    P_plus = Pplus(x_)
    P_minus = Pminus(LD)
    Z = Cond_Entro(P_plus, P_minus, p)
    
    fig, ax = plt.subplots()
    #ax.set_xscale("log")
    #ax.set_yscale("log")
    pcm = ax.pcolormesh(X, Y, Z,
                       cmap='jet_r', shading='nearest')
    ax.set_xlabel('FP')
    ax.set_ylabel('FN')
    ax.set_title('Conditional Entropy given p %.2f' %p)
    
    fig.colorbar(pcm, ax=ax, extend='max')
    CS = ax.contour(X, Y, Z, cmap='Greys')
    ax.clabel(CS, inline=True, fontsize=10)


