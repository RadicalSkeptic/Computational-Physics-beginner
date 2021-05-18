from vpython import *
from numpy import *
n = 10
i = 0
y = zeros(1000)
func = gdots(color=color.red)
while(i <= 999):
    y[i] = n
    n = (57*n+1) % 256
    i += 1
for x in arange(0, 1000, 1):
    func.plot(pos=(x, y[x]))
