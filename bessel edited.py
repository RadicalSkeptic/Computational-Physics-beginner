from vpython import *
from numpy import *

Xmax = 40
Xmin = .25
step = .1
order = 10
start = 50
graph1 = graph(width=500, height=500, title='Spherical Bessel, L=1(red), 10',
               xtitle='x', ytitle='j(x)', xmin=Xmin, xmax=Xmax, ymin=-.2, ymax=.5)
funct1 = gcurve(color=color.red)
funct2 = gcurve(color=color.green)


def down(x, n, m):
    j = zeros(start+2, float)
    j[m+1] = j[m] = 1.
    for k in range(m, 0, -1):
        j[k-1] = ((2.*k+1)/x)*j[k]-j[k+1]
    scale = (sin(x)/x)/j[0]
    return j[n]*scale


def up(x, n, m):
    j = zeros(start+2, float)
    j[1] = j[0] = 1.
    for k in range(0, m, 1):
        j[k+1] = ((2.*k+1)/x)*j[k]-j[k-1]
    scale = (sin(x)/x)/j[0]
    return j[n]*scale


for x in arange(Xmin, Xmax, step):
    funct1.plot(pos=(x, down(x, order, start)))

for x in arange(Xmax, Xmin, step):
    funct2.plot(pos=(x, up(x, order, start)))
