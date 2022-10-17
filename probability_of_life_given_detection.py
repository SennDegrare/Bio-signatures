from pylab import figure, cm

import matplotlib.pyplot as plt
import numpy as np


def f(x1,x2): #x1 = y = P(fn), x2 = z = P(fp)
    return ((x1-1)*(x2*np.log(abs((1-x1)/x2))+x1+x2-1))/((x1+x2-1)**2)
x1_min = 0
x1_max = 1
x2_min = 0
x2_max = 1
#Problem with the limits: denominator has values = 0.
x1, x2 = np.meshgrid(np.arange(x1_min,x1_max, 0.01), np.arange(x2_min,x2_max, 0.01))
y = f(x1,x2)
plt.imshow(y,extent=[x1_min,x1_max,x2_min,x2_max]) 

plt.colorbar()

plt.title("P(L|D)" , fontsize=8)

plt.savefig("probability_of_life_given_detection.png", bbox_inches='tight')

plt.show()

