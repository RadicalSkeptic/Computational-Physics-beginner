from numpy import arange, zeros
import vpython as vp
import cmath as cm

from vpython.vpython import color, graph


N = 500
h = 2*cm.pi/N
range = 2*cm.pi
points = 500
step = range/points


def y(t):
    # return cm.sin(5*t)+2*cm.cos(3*t)+5*cm.sin(t)
    # return 5+10*cm.sin(t+2)
    # return 7
    return 3*cm.sin(5*t)+2*cm.sin(3*t)+cm.sin(t)


Ys = zeros((N+1), complex)


def Y(x):
    Y1 = 0
    for k in arange(1, N+1, 1):
        Y1 += h*cm.exp(-1j*2*cm.pi*x*k/N)*y(k*h)/cm.pi

    # if x == 0 or x == N:
    #    Y1 /= 2
    #Ys[x] = Y1*cm.sqrt(cm.pi/2)
    Ys[x] = Y1
    # return Y1/1.253314105
    return Y1.real, Y1.imag


def yr(t):
    y1 = 0
    for x in arange(1, N+1, 1):
        y1 += Ys[x]*cm.exp(1j*2*cm.pi*x*t/(h*N))/2
    print(y1)
    print(y1.real-y1.imag)
    return y1.real


yg = vp.graph(title='Function', xtitle='t', ytitle='y(t)', fast=False)
Yg = vp.graph(title='Fourier', xtitle='x', ytitle='Y(x)', fast=False)
yc = vp.graph(title='Resum', xtitle='t', ytitle='y(t)', fast=False)
func = vp.gcurve(graph=yg, color=vp.color.blue)
fourcos = vp.gvbars(graph=Yg, color=vp.color.red)
foursin = vp.gvbars(graph=Yg, color=vp.color.green)
funcre = vp.gcurve(graph=yc, color=vp.color.blue)

for i in arange(0, range, step):
    func.plot(i, y(i).real)


for i in arange(0, N+1, 1):
    Yn = Y(i)
    fourcos.plot(i, Yn[0])
    foursin.plot(i, -Yn[1])

for i in arange(0, range, step):
    funcre.plot(i, yr(i))
