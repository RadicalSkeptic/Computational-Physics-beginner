from vpython import *
from numpy import *
from random import *

y = zeros(1000)
i = 0

func = gdots(color=color.red)
while(i <= 999):
    y[i] = random()
    i += 1
for x in arange(0, 999, 1):
    func.plot(pos=(x, y[x]))
