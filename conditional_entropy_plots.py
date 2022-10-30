import numpy as np
from matplotlib import pyplot as plt


FPs = np.arange(0.01,1.00,0.01)
FNs = np.arange(0.01,1.00,0.01)
fs = np.arange(0.01,1.00,0.01)
fs_log = 10**-np.arange(0.01,10,0.01)
f1=.001

def PLgD(FP,FN,f):
    # probability of life given detection
    return (1-FN)*f/((1-FN)*f+FP*(1-f))

def PLgND(FP,FN,f):
    # probability of life given nondetection
    return FN*f/(FN*f+(1-FP)*(1-f))

def PD(FP,FN,f):
    # probability of detection
    return (1-FN)*f+FP*(1-f)

def S(p):
    return p*np.log(p)+(1-p)*np.log(1-p)

def Sr(Pld,Pd):
    # conditional entropy
    return -Pld*Pd*np.log(Pld)-(1-Pld)*Pd*np.log(1-Pld)

def make_subplot(ax,X,Y,Z,title=''):
    ax.set(aspect=1)
    ax.set_ylabel('FN')
    ax.set_xlabel('FP')
    ax.set_title(title)

    pcm = ax.pcolormesh(X, Y, Z,
                        cmap='jet_r', 
                        shading='nearest')
    #fig.colorbar(pcm, ax=ax)
    CS = ax.contour(X, Y, Z)
    ax.clabel(CS, inline=True,fontsize=10)
    
    
X,Y = np.meshgrid(FPs,FNs)
Z1 = Sr(PLgD(X,Y,f1),PD(X,Y,f1)) + Sr(PLgND(X,Y,f1),1-PD(X,Y,f1))

X,Y,F = np.meshgrid(FPs,FNs,fs)
Z2 = Sr(PLgD(X,Y,F),PD(X,Y,F)) + Sr(PLgND(X,Y,F),1-PD(X,Y,F))
Z2 = np.mean(Z2,axis=2)

X,Y,F2 = np.meshgrid(FPs,FNs,fs_log)
Z3 = Sr(PLgD(X,Y,F2),PD(X,Y,F2)) + Sr(PLgND(X,Y,F2),1-PD(X,Y,F2))
Z3 = np.mean(Z3,axis=2)

X=X[:,:,0]
Y=Y[:,:,0]


fig, axs = plt.subplots(1,3,figsize=(10,5))

make_subplot(axs[0], X, Y, Z1,'f='+str(f1))
make_subplot(axs[1], X, Y, Z2,'uniform')
make_subplot(axs[2], X, Y, Z3,'log-uniform')

plt.tight_layout()
plt.savefig('conditional_entropy.png',bbox_inches='tight')
plt.show()