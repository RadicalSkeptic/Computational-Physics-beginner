import random
from vpython import *

N = 100
graph1 = graph(width=500, height=500, title='vonNeuman Rejection Int')
xsinx = curve(x=list(range(0, N)), color=color.yellow, radius=.5)
pts = label(pos=(-60, -60), text='points=', box=0)
pts2 = label(pos=(-30, -60), box=0)
inside = label(pos=(30, -60), text='accepted=', box=0)
inside2 = label(pos=(60, -60), box=0)
arealbl = label(pos=(-65, 60), text='area=', box=0)
arealbl2 = label(pos=(-35, 60), box=0)
areanal = label(pos=(30, 60), text='analytical=', box=0)
zero = label(pos=(-85, -48), text='0', box=0)
five = label(pos=(-85, 50), text='5', box=0)
twopi = label(pos=(90, -48), text='2pi', box=0)


def fx(x): return x*sin(x)*sin(x)


def plotfunc():
    incr = 2*pi/N
    for i in range(0, N):
        xx = i*incr
        xsinx.x[i] = ((80/pi)*xx-80)
        xsinx.y[i] = 20*fx(xx)-50
    box = curve(pos=[(-80, -50), (-80, 50), (80, 50),
                (80, -50), (-80, -50)], color=color.white)


plotfunc()
j = 0
Npts = 3001
analyt = pi**2
areanal.text = 'analytical=%8.5f' % analyt
genpts = points(size=2)
for i in range(1, Npts):
    rate(500)
    x = 2*pi*random.random()
    y = random.random()
    xp = x*80/pi-80
    yp = 20*y-50
    pts2.text = '%4s' % i
    if y <= fx(x):
        j += 1
        genpts.append(pos=(xp, yp), color=color.cyan)
        inside2.text = '%4s' % j
    else:
        genpts.append(pos=(xp, yp), color=color.green)
    boxarea = 10*pi
    area = boxarea*j/(Npts-1)
    arealbl2.text = '%8.5f' % area
