import scipy as sp
import numpy as np
from scipy import integrate as integ

m = .5


def f(x): return (1-m*(np.sin(x))**2)**(-.5)


i = integ.fixed_quad(f, 0, np.pi/2, n=1000)

print(i)

j = integ.quadrature(f, 0, np.pi/2)

print(j)
