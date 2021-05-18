from numpy import *

m = 15
c = 1
x = zeros(2**m)
for n in arange(0, m, 1):
    for i in arange(0, 2**n, 1):
        if x[i] == 0:
            x[c] = 1
        c += 1
print(x)
