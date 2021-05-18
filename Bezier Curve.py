from numpy import *
import vpython as vp

x = array([0, 0, 2])
y = array([2, 0, 2])

graph1 = vp.graph(title="Quadratic Bezier", width=500, height=500)
func1 = vp.gdots(color=vp.color.red)
for i in range(0, 3):
    func1.plot(x[i], y[i])

divs = 1000
func2 = vp.gcurve(color=vp.color.blue)
for i in arange(0, divs+1, 1):
    x1 = x[0]+(x[1]-x[0])*i/divs
    x2 = x[1]+(x[2]-x[1])*i/divs
    y1 = y[0]+(y[1]-y[0])*i/divs
    y2 = y[1]+(y[2]-y[1])*i/divs
    vp.rate(100)
    func2.plot(x1+i*(x2-x1)/divs, y1+i*(y2-y1)/divs)
