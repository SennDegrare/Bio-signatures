from matplotlib import pyplot as plt
import numpy as np
import matplotlib.patheffects as pe
from scipy.stats import norm

survey =[
("Mercury", u"\u263F",250,1),
("Mercury", u"\u263F",40,0),
("Venus", u"\u2640",1000,1),
("Venus", u"\u2640",10,10**-9),
("Earth", "E",.1,1/3),
("L1, L2", "L1",30,.01),
("L3, L4, L5", "L3",3,.01),
("Moon", u"\u263E",.5,1),
('Mars', u"\u2642",1,.01),
('Mars', u"\u2642",100,1),
('Ceres', "C",410,1),
('Jupiter', u"\u2643",6000,0),
('Saturn', u"\u2644",3000,0),
('Uranus', u"\u26E2",10000,0),
('Neptune', u"\u2646",3000,1/3),
('Pluto', u"\u2647",33,1)
]

def prob(p, D, f_R, N):
    cdf = norm.cdf(D,1,.5)
    #cdf = 1-np.exp(-D)
    #cdf = 1-1/(D+10**-6)
    prob_var = p*(1-cdf+(1-f_R)**N*cdf)/(1-p*(1-(1-f_R)**N)*cdf)
    return prob_var

fig, axs = plt.subplots(1,1,figsize=(20,10))

f_Rc = np.arange(0.001,1.00,0.001)
Dc = np.arange(0,1000,.001)
Dc = 10**np.arange(-3.7,3,.01)

Xc,Yc = np.meshgrid(Dc,f_Rc)
Zc = prob(p=.5,D=Xc,f_R=Yc,N=10)
#Zc = S(Zc)


def make_subplot_c(ax,X,Y,Z,title='',whitedash=True):
    #ax.set(aspect=X.shape[1]/X.shape[0])
    ax.set_xlabel('R / D')
    ax.set_ylabel('$f_R$')
    ax.set_title(title)


    pcm = ax.pcolormesh(X, Y, Z,
                   cmap='jet_r', shading='nearest')
    fig.colorbar(pcm, ax=ax)
    CS = ax.contour(X, Y, Z)
    ax.clabel(CS, inline=True,fontsize=10)

    if whitedash:
        ax.plot([1,1],[0,1],c='white',linewidth=3,linestyle='--')
    ax.set_ylim(0,1)
    
make_subplot_c(axs,Xc,Yc,Zc,title='p(N>0|null),  $p^*=.5$,  $N^*=10$')

for n,c,d,a in survey:
    print(n,c)
    if a<.001:
        a=.5
    plt.text(10/d,a*.7,c,fontsize=40,color='black',
             path_effects=[pe.withStroke(linewidth=6, foreground="white")])
    #plt.text(10/d,a*.7,c,fontsize=35,color='black')
plt.xscale('log')
plt.yscale('log')
plt.ylim(5*10**-3,1)
plt.savefig('lurker_points.png',bbox_inches='tight')
plt.show()