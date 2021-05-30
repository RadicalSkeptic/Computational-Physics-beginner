from os import system
import os
from numpy import append, array, empty
from vpython import *
import pylab as plb

step = .001
xa = []
ya = []
m_min = 2.5
m_max = 6

t = (m_max-m_min)/(step)**3


for m in arange(m_min, m_max, step):
    y = .5
    d = (m-m_min)/(step)**3
    for i in arange(0, 300, 1):
        y = y*exp(m*(1-y))
    for i in arange(0, 1/step**2, 1):
        y = y*exp(m*(1-y))
        if i == 0:
            last0 = y
        elif i == 1:
            last1 = y
        elif i == 2:
            last2 = y
        elif i == 3:
            last3 = y
        elif int(last0/step) == int(y/step) or int(last1/step) == int(y/step) or int(last2/step) == int(y/step) or int(last3/step) == int(y/step):
            break
        xa.append(m)
        ya.append(int(y/step)*step)
        # ya.append(y)
        print((d+i)/t*100, "%", m)

plb.plot(xa, ya, 'b+', markersize=1)
plb.show()
