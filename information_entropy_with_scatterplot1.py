#Information Entropy of Life Given Detection #S = -Pln(p) - (1-p)ln(1-p)
from pylab import figure, cm

import matplotlib.pyplot as plt
import numpy as np
from pylab import meshgrid,cm,imshow,contour,clabel,colorbar,axis,title,show

def f(x1,x2):
    return -((x1 - 1) * (x2 * np.log((1 - x1) / (x2)) + x1 + x2 - 1)) / ((x1 + x2 - 1)**2) * np.log(((x1 - 1) * (x2 * np.log((1 - x1) / (x2)) + x1 + x2 - 1)) / ((x1 + x2 - 1)**2)) - (1 - (((x1 - 1) * (x2 * np.log((1 - x1) / (x2)) + x1 + x2 - 1)) / ((x1 + x2 - 1)**2))) * np.log(1 - (((x1 - 1) * (x2 * np.log((1 - x1) / (x2)) + x1 + x2 - 1)) / ((x1 + x2 - 1)**2)))

x1_min = 0
x1_max = 1 #P(fn)
x2_min = 0
x2_max = 1#P(fp)

x1, x2 = np.meshgrid(np.arange(x1_min,x1_max, 0.01), np.arange(x2_min,x2_max, 0.01))

y = f(x1,x2)

probabilities_of_false_positives = [0.3, 0.4, 0.5]
probabilities_of_false_negatives = [0.3, 0.4, 0.2]


# probabilities_of_false_positives = [0.8, 0.75, 0.73, 0.74, 0.5, 0.49, 0.43, 0.42, 0.41, 0.3, 0.15, 0.2, 0.1, 0.16, 0.05, 0.07, 0.03, 0.2, 0.25]
# probabilities_of_false_negatives = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95]
plt.ylabel('P(fp)')  
plt.xlabel('P(fn)')
for (probability1, probability2) in zip(probabilities_of_false_positives, probabilities_of_false_negatives):
    plt.scatter(x = probability2, y = probability1)
plt.imshow(y,extent=[x1_min,x1_max,x2_min,x2_max], cmap=cm.jet, origin='lower')

plt.colorbar()

plt.title("S = -Pln(p) - (1-p)ln(1-p)", fontsize=10)

plt.savefig("information_gain_probability_of_life_given_detection.png")

plt.show()
