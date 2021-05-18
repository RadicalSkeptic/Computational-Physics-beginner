import random as rn
import numpy as np
import pylab as p

x = np.array([-1, 0, 1])
y = np.array([0, np.sqrt(5), 0])

iter = 100000000
n = np.zeros(iter)
m = np.zeros(iter)
list = np.array([0, 1, 2])

for i in np.arange(0, iter-1, 1):
    rnd = rn.choice(list)
    n[i+1] = (n[i]+x[rnd])/2
    m[i+1] = (m[i]+y[rnd])/2

p.plot(n, m, 'ro', markersize=.1)
p.show()
