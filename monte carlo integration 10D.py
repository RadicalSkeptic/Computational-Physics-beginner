import numpy as np
import random as rand

n = 1000000
dimen = 10


def z(a):
    k = 0
    for i in np.arange(0, dimen, 1):
        k += a[i]
    return k**2


xleft = 0
xright = 1
yup = 100
ydown = 0

nin = 0

for f in np.arange(0, n, 1):
    r = rand.uniform(ydown, yup)
    x = np.zeros(10)
    for j in np.arange(0, dimen, 1):
        x[j] = rand.uniform(xleft, xright)
    if r > 0:
        if r < z(x):
            nin += 1
    if r < 0:
        if r > y(x):
            nin -= 1


d = (xright-xleft)**dimen*(yup-ydown)*nin/n
print(d)
