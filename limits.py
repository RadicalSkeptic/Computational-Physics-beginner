import numpy as p
n = 100
eps = p.longdouble(1.0)
for i in range(n):
    eps = eps/2
    one_plus_eps = 1.0+eps
    print("eps = ", eps, "one + eps = ", one_plus_eps)
