import scipy as sp
import numpy as np
from scipy import integrate as integ


def f(x): return x**9


i = integ.fixed_quad(f, 0, 1, n=1000)

print(i)

j = integ.quadrature(f, 0, 1)

print(j)
