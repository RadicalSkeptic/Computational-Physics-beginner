import random as rand
import numpy as np
import vpython as vp

n = 100  # Number of divisions between 0 and iter
f = np.zeros(n)
iter = 10
num = 1000000  # Number of dots


def func():
    x = 0
    for i in np.arange(0, iter, 1):
        x += rand.random()
    return x


graph1 = vp.graph(title='Gaussian Distribution')
func0 = vp.gcurve(color=vp.color.blue)

for a in np.arange(0, num, 1):
    d = func()
    z = round(d*n/iter)-1
    f[z] += 1
    #func0.plot(d, f[z])

for e in np.arange(0, n, 1):
    if f[e] != 0:
        func0.plot(e*iter/n, f[e])
