import pylab as p
#from numpy import *
import numpy as np
import scipy.integrate as sp

i = 20  # change this


def an(n):
    result = sp.quad(lambda x: np.sin(x)*np.cos(n*x), 0, np.pi)
    return result[0]/np.pi


def bn(n):
    result = sp.quad(lambda x: np.sin(x)*np.sin(n*x), 0, np.pi)
    return result[0]/np.pi


def fourier(n):
    x = np.arange(-5, 5, .1)
    y = an(n)*np.cos(n*x)+bn(n)*np.sin(n*x)
    return y


y1 = np.zeros(100)
x = np.arange(-5, 5, .1)

for v in np.arange(0, i, 1):
    for n in np.arange(1, v, 1):
        y1 += fourier(n)
        n += 1
    y1 += 1/np.pi
    p.plot(x, y1)
    p.show()
    y1 = np.zeros(100)
