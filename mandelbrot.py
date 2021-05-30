from os import system
import os
from numpy import append, array, conjugate, empty
from numpy.core.numeric import full
from vpython import *
import pylab as plb

step = .001
xa = []
ya = []
nx = int((2+.47)/step+1)
ny = int((2*1.12)/step+1)
xa = 0
ya = 0
t = 2.47*2.24/(step**2)
img = full((ny, nx), 255)

for x in arange(-2, .47, step):
    d = (x+2)*2.24/(step**2)
    print(d/t*100, "%")
    for y in arange(-1.12, 1.12, step):
        z = 0
        i = 0
        while i < 25 and (z*z.conjugate()).real < 4:
            z = z**2+x+y*1j
            i += 1
        img[ya][xa] = 255-i
        ya += 1
    xa += 1
    ya = 0
'''        if z*z.conjugate().real < 4:
            xa.append(x)
            ya.append(y)'''

plb.imshow(img, cmap="plasma")
#plb.plot(xa, ya, 'b+', markersize=1)
plb.show()
