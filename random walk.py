import random
from numpy import *
import pylab as p
steps = 1000
x1 = zeros(steps)
y1 = zeros(steps)
for i in arange(1, steps, 1):
    x1[i] = x1[i-1]+((random.random()-.5)*2)
    y1[i] = y1[i-1]+((random.random()-.5)*2)
p.plot(x1, y1)
p.show()
