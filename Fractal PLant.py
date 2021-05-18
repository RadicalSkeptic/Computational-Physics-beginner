import vpython as vp
import random as rn

imax = 20000
x = .5
y = 0.0

xn = 0.0
yn = 0.0

graph1 = vp.graph(width=500, height=500,
                  title='3D Fractal Plant')

pts = vp.gdots(color=vp.color.green, radius=.1)
for i in range(1, imax):
    r = rn.random()
    if r <= .1:
        xn = 0.05*x
        yn = .6*y

    elif r > .1 and r <= .2:
        xn = .05*x
        yn = -.05*y+.1

    elif r > .2 and r <= .4:
        xn = .46*x-.15*y
        yn = .39*x+.38*y+.6

    elif r > .4 and r <= .6:
        xn = -.47*x-.15*y
        yn = .17*x+.42*y+1.1

    elif r > .6 and r <= .8:
        xn = -.43*x+.28*y
        yn = -.25*x+.45*y+1

    else:
        xn = .42*x+.26*y
        yn = -.35*x+.31*y+.7

    x = xn
    y = yn
    xc = 4*x
    yc = 2*y-7
    pts.plot(xc, yc)
