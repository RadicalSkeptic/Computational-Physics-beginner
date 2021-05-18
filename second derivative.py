import numpy as np
import vpython as vp


def y(t):
    f = np.cos(t)
    return f


graph1 = vp.graph(title='fd1 blue, fd2 red',
                  xtitle='log10 h', ytitle='log10 error')
func1 = vp.gdots(color=vp.color.blue, )
func2 = vp.gdots(color=vp.color.red)

x = 100
d = -np.cos(x)

for a in np.arange(0, 20, 1):
    h = .1**a
    fd1 = ((y(x+h)-y(x))-(y(x)-y(x-h)))/h**2
    print("\nfd1=", fd1)
    print("h=", h, ">>", (fd1-d)/d)
    func1.plot((np.log10(h), np.log10((fd1-d)/d)))

for a in np.arange(0, 20, 1):
    h = .1**a
    fd2 = (y(x+h)+y(x-h)-2*y(x))/h**2
    print("\nfd2=", fd2)
    print("h=", h, ">>", (fd2-d)/d)
    func2.plot((np.log10(h), np.log10((fd2-d)/d)))
