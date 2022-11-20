import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from scipy.stats import norm


def prob(p, D, f_R, N):
    cdf = norm.cdf(D,1,.5)
    prob_var = p*(1-cdf+(1-f_R)**N*cdf)/(1-p*(1-(1-f_R)**N)*cdf)
    return prob_var

def powerlawcdf(D):
    c = 1-1/(D+10**-6)
    return c*(c>0)

def prob_pl(p, D, f_R, N):
    cdf = powerlawcdf(D)
    prob_var = p*(1-cdf+(1-f_R)**N*cdf)/(1-p*(1-(1-f_R)**N)*cdf)
    return prob_var

def prob_opt(p, D, f_R, N):
    cdf = norm.cdf(D,1,.5)
    prob_var = (1-(1-f_R)**N)*cdf
    return prob_var



def make_subplot_Df(ax,X,Y,Z,title='',whitedash=True):
    ax.set(aspect=X.shape[1]/X.shape[0])
    ax.set_xlabel('D / R')
    ax.set_ylabel('$f_R$')
    ax.set_title(title)


    pcm = ax.pcolormesh(X, Y, Z,
                   cmap='jet_r', shading='nearest')
    fig.colorbar(pcm, ax=ax)
    CS = ax.contour(X, Y, Z)
    ax.clabel(CS, inline=True,fontsize=10)

    xs = np.arange(.1,10,.01)
    ax.plot(xs,np.arctan(1/xs),c='black',linestyle='--')
    if whitedash:
        ax.plot([1,1],[0,1],c='white',linewidth=3,linestyle='--')
    ax.set_ylim(0,1)

def make_subplot_pN(ax,X,Y,Z,title='',whitedash=True):
    ax.set(aspect=X.shape[0]/X.shape[1])
    ax.set_xlabel('$p^*$')
    ax.set_ylabel('$N^*$')
    ax.set_title(title)


    pcm = ax.pcolormesh(X, Y, Z,
                   cmap='jet_r', shading='nearest')
    fig.colorbar(pcm, ax=ax)
    CS = ax.contour(X, Y, Z)
    ax.clabel(CS, inline=True,fontsize=10)

    
f_R = np.arange(0.01,1.00,0.01)
D = np.arange(0,10,0.01)

X,Y = np.meshgrid(D,f_R)
Z1 = prob(p=.5,D=X,f_R=Y,N=1)
Z2 = prob(p=.9,D=X,f_R=Y,N=1)
Z3 = prob(p=.5,D=X,f_R=Y,N=10)
Z4 = prob_pl(p=.5,D=X,f_R=Y,N=1)
Z5 = 1-prob_opt(p=.5,D=X,f_R=Y,N=1)

ps = np.arange(0.01,1.00,0.01)
Ns = np.arange(1,11,1)
X2,Y2 = np.meshgrid(ps,Ns)
Z6 = prob(p=X2,D=2,f_R=.2,N=Y2)


fig, axs = plt.subplots(2,3,figsize=(18,10))

make_subplot_Df(axs[0][0],X,Y,Z1,title='p(N>0|null),  $p^*=.5$,  $N^*=1$')
make_subplot_Df(axs[0][1],X,Y,Z2,title='$p^*=.9$,  $N^*=1$')
make_subplot_Df(axs[0][2],X,Y,Z3,title='$p^*=.5$,  $N^*=10$')
make_subplot_Df(axs[1][1],X,Y,Z4,title='power law,  $p^*=.5$,  $N^*=1$')
make_subplot_Df(axs[1][0],X,Y,Z5,title='p(det|N>0),  $p^*=.5$,  $N^*=1$')
make_subplot_pN(axs[1][2],X2,Y2,Z6,title='$f_R=.2$,  D/R=2')

plt.tight_layout()
plt.savefig('lurker_plots.png',bbox_inches='tight')
plt.show()