
from math import pi, sin
from scipy import fftpack as ff
import numpy as np
import vpython as vp
from vpython.vpython import color, gcurve, gdots, graph, gvbars
import cmath as cm

step = .001
w0 = 8
range = 2*np.pi
t = np.arange(-range, range, step)
sig = np.sin(w0*t)
#sig = np.e**(-t**2/2)*np.sin(w0*t**2)

fltr = np.zeros(int(2*range/step)+1)
for i in np.arange(int(range/step-pi/2/step), int(range/step+pi/2/step+1), 1):
    fltr[i] = 1

sig *= fltr

sigfft = ff.fft(sig, sig.size*10)*7/4.41e3
sigfreq = ff.fftfreq(sig.size*10, step*10)*2*np.pi
print(sig.size)
resum = ff.ifft(sigfft)*4.41e3/7
sigfft[0] /= 2

graphsig = graph(title='signal', fast=False)
sigcur = gcurve(graph=graphsig, color=color.blue)
graphfft = graph(title='FFT', fast=False)
fftsin = gcurve(graph=graphfft, color=color.green)
fftcos = gcurve(graph=graphfft, color=color.red)
graphsum = graph(title='resum', fast=False)
sigsum = gcurve(graph=graphsum, color=color.blue)

for i in np.arange(0, 2*range/step, 1):
    z = int(i)
    sigcur.plot(t[z], sig[z])
    fftsin.plot(sigfreq[z], -sigfft[z].imag)
    fftcos.plot(sigfreq[z], sigfft[z].real)
    sigsum.plot(t[z], resum[z].real)
