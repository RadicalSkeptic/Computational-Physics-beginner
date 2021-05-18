import scipy as sp
import numpy as np
from scipy import integrate as integ

m = float(input("Enter maximum angle of displacement in radian: "))
t0 = float(input("Enter period for small angle approximation: "))


def f(x): return ((np.sin(m/2))**2 - (np.sin(x/2))**2)**(-.5)


i = integ.fixed_quad(f, 0, m, n=1000)

print(t0*i[0]/np.pi)

j = integ.quadrature(f, 0, m)

print(t0*j[0]/np.pi, t0*j[1]/np.pi)
