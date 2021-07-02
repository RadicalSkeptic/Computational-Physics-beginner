import math
from scipy.optimize import fsolve
from math import exp


def equations(p):
    x1, x2, x3, x4, x5, x6, x7, x8, x9 = p
    return (3*x4+4*x5+4*x6-8, 3*x1+4*x2-4*x3,
            x7*x1-x8*x2-10, x7*x4-x8*x5,
            x8*x2+x9*x3-20, x8*x5-x9*x6,
            x1**2+x4**2-1, x2**2+x5**2-1,
            x3**2+x6**2-1)


x1, x2, x3, x4, x5, x6, x7, x8, x9 = fsolve(
    equations, (1, 1, 1, 1, 1, 1, 1, 1, 1))

print(x1, x2, x3, x4, x5, x6, x7, x8, x9)
print(equations((x1, x2, x3, x4, x5, x6, x7, x8, x9)))
