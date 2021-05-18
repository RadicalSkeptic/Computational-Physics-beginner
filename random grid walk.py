import random
from numpy import *

import pylab as p
steps = 1000
x = zeros(steps)
y = zeros(steps)

list = array([1, 2, 3, 4])

for i in arange(1, steps, 1):
    f = random.choice(list)
    x[i] = x[i-1]
    y[i] = y[i-1]
    if (f == 1):
        x[i] += 1
    elif(f == 2):
        y[i] += 1
    elif(f == 3):
        x[i] -= 1
    elif(f == 4):
        y[i] -= 1
    else:
        print("ERROR!")

p.plot(x, y)
p.grid(True)
p.show()
