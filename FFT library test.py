from scipy import fftpack as ff
import numpy as np
import vpython as vp
from vpython.vpython import color, gcurve, graph, gvbars
import cmath as cm

step = .01
range = 2*np.pi
t = np.arange(0, range, step)
#sig = np.sin(np.pi*t/2)+np.sin(2*np.pi*t)
#sig = np.full((t.size), 7)
#sig = 3*np.sin(5*t)+2*np.sin(3*t)+np.sin(t)
#sig = np.sin(5*t)+2*np.cos(3*t)+5*np.sin(t)
sig = np.sinc(t)

sigfft = ff.fft(sig)*14/4.41e3
sigfreq = ff.fftfreq(sig.size, step)*2*np.pi
resum = ff.ifft(sigfft)*4.41e3/14
sigfft[0] /= 2

graphsig = graph(title='signal', fast=False)
sigcur = gcurve(graph=graphsig, color=color.blue)
graphfft = graph(title='FFT', fast=False)
fftsin = gvbars(graph=graphfft, color=color.green)
fftcos = gvbars(graph=graphfft, color=color.red)
graphsum = graph(title='resum', fast=False)
sigsum = gcurve(graph=graphsum, color=color.blue)

for i in np.arange(0, range/step, 1):
    z = int(i)
    sigcur.plot(t[z], sig[z])
    fftsin.plot(sigfreq[z], -sigfft[z].imag)
    fftcos.plot(sigfreq[z], sigfft[z].real)
    sigsum.plot(t[z], resum[z].real)
