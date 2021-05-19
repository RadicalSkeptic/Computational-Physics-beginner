from numpy.lib.function_base import sinc
from scipy import fftpack as ff
import numpy as np
import vpython as vp
from vpython.vpython import color, gcurve, graph, gvbars
import cmath as cm
from numpy import random

k = 313
step = .01
range = 2*np.pi
t = np.arange(0, range, step)
rd = random.rand(t.size)
#sig = np.sin(np.pi*t/2)+np.sin(2*np.pi*t)
#sig = np.full((t.size), 7)
sig = 3*np.sin(5*t)+2*np.sin(3*t)+np.sin(t)+10*(rd-.5)
#sig = np.sin(5*t)+2*np.cos(3*t)+5*np.sin(t)
#sig = np.sin(t)+2*(rd-.5)
'''sig = np.sin(2*t)/t
sig[0] = 2'''

sigfft = ff.fft(sig)/k
sigfreq = ff.fftfreq(sig.size, step)*2*np.pi
resum = ff.ifft(sigfft)*k
sigfft[0] /= 2

graphsig = graph(title='signal', fast=False)
sigcur = gcurve(graph=graphsig, color=color.blue)
graphfft = graph(title='FFT', xtitle='omega', ytitle='amplitude', fast=False)
fftsin = gvbars(graph=graphfft, color=color.green)
fftcos = gvbars(graph=graphfft, color=color.red)
graphsum = graph(title='resum', fast=False)
sigsum = gcurve(graph=graphsum, color=color.blue)


def filtr():
    wc = 10
    fltr = np.zeros(int(range/step))
    for i in np.arange(0, range/step, 1):
        l = int(i)
        if abs(sigfreq[l]) > wc:
            sigfft[l] = 0
    resum = ff.ifft(sigfft)*k
    for i in np.arange(0, range/step, 1):
        z = int(i)
        sigsum.plot(t[z], resum[z].real)
        fftsin.plot(sigfreq[z], -sigfft[z].imag)
        fftcos.plot(sigfreq[z], sigfft[z].real)


for i in np.arange(0, range/step, 1):
    z = int(i)
    sigcur.plot(t[z], sig[z])
'''    fftsin.plot(sigfreq[z], -sigfft[z].imag)
    fftcos.plot(sigfreq[z], sigfft[z].real)'''

filtr()
