import numpy as np
import random as rand

n = 1000000
def y(a): return a**9


xleft = 0
xright = 2*np.pi
yup = (2*np.pi)**9
ydown = 0

nin = 0
nout = 0
for f in np.arange(0, n, 1):
    r = rand.uniform(ydown, yup)
    x = rand.uniform(xleft, xright)
    if r > 0:
        if r < y(x):
            nin += 1
        else:
            nout += 1
    if r < 0:
        if r > y(x):
            nin -= 1
        else:
            nout += 1


d = (xright-xleft)*(yup-ydown)*nin/(nout+nin)
print(d)
