import numpy as np
import random as rand

n = 1000000

npond = 0
nbox = 0
for f in np.arange(0, n, 1):
    if ((rand.random()-.5)*2)**2+((rand.random()-.5)*2)**2 < 1:
        npond += 1
    else:
        nbox += 1

a = 4*npond/(npond+nbox)
print(a)
