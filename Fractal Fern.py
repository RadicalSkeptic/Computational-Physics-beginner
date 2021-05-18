import vpython as vp
import random as rn

imax = 20000
x = .5
y = 0.0
z = -.2
xn = 0.0
yn = 0.0

graph1 = vp.graph(width=500, height=500, forward=(-3, 0, -1),
                  title='3D Fractal Fern (rotate via right mouse button)', range=10)
graph1.show_rendertime = True

pts = vp.points(color=vp.color.green, markersize=.001)
for i in range(1, imax):
    r = rn.random()
    if r <= .1:
        xn = 0
        yn = -.18*y
        zn = 0
    elif r > .1 and r <= .7:
        xn = .85*x
        yn = .85*y+.1*z+1.6
        zn = -.1*y+.85*x
    elif r > .7 and r <= .85:
        xn = .2*x-.2*y
        yn = .2*x+.2*y+.8
        zn = .3*z
    else:
        xn = -.2*x+.2*y
        yn = .2*x+.2*y+.8
        zn = .3*z
    x = xn
    y = yn
    z = zn
    xc = 4*x
    yc = 2*y-7
    zc = z
    pts.append(pos=(xc, yc, zc))
