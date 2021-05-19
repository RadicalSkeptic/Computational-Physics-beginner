from matplotlib.pyplot import title
from vpython import *
from numpy import *
import cmath
signgr = graph(x=0, y=0, width=600, height=250, title='signal', xtitle='x', ytitle='signal',
               xmax=2*pi, xmin=0, ymax=30, ymin=0, fast=False)
sigfig = gcurve(graph=signgr, color=color.yellow)

imagr = graph(x=0, y=250, width=600, height=250, title='Image Fourier TF',
              xtitle='x', ytitle='TF.imag', xmax=10, xmin=-1, ymax=100, ymin=-.2, fast=False)
impart = gvbars(graph=imagr, delta=.05, color=color.red)

N = 5000
Np = N
signal = zeros((N+1), float)
twopi = 2*pi
sq2pi = 1/sqrt(twopi)
h = twopi/N
dftz = zeros((Np), complex)


def f(signal):
    step = twopi/N
    x = 0
    for i in range(0, N+1):
        signal[i] = 3
        sigfig.plot(pos=(x, signal[i]))
        x += step


def fourier(dftz):
    for n in range(0, Np):
        zsum = complex(0.0, 0.0)
        for k in range(0, N):
            zexpo = complex(0, twopi*k*n/N)
            zsum += signal[k]*exp(-zexpo)
        dftz[n] = zsum*sq2pi
        if dftz[n].imag != 0:
            impart.plot(pos=(n, dftz[n].imag))


f(signal)
fourier(dftz)
