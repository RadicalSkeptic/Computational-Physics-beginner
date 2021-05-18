import scipy.interpolate as sp
from numpy import *
import vpython as vp

n = 9

x = array([0, 25, 50, 75, 100, 125, 150, 175, 200])
y = array([10.6, 16, 45, 83.5, 52.8, 19.9, 10.8, 8.25, 4.7])


graph1 = vp.graph(title="Cubic Spline Interpolation")
func1 = vp.gdots(color=vp.color.red)
for i in arange(0, n, 1):
    func1.plot(x[i], y[i])

cs = sp.CubicSpline(x, y)

max = x[0]
min = x[0]

for t in arange(0, n, 1):
    if x[t] > max:
        max = x[t]
    if x[t] < min:
        min = x[t]

func2 = vp.gcurve(color=vp.color.blue)
divs = 10000
for e in arange(0, divs+1, 1):
    func2.plot(min+e*(max-min)/divs, cs(min+e*(max-min)/divs))
