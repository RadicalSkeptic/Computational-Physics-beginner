import numpy as np
import vpython as vp


def y(t):
    f = np.cos(t)
    return f


graph1 = vp.graph(title='fd blue, cd red, ed green',
                  xtitle='log10 h', ytitle='log10 error')
func1 = vp.gdots(color=vp.color.blue, )
func2 = vp.gdots(color=vp.color.red)
func3 = vp.gdots(color=vp.color.green)
x = 100
d = -np.sin(x)

for a in np.arange(0, 20, 1):
    h = .1**a
    fd = (y(x+h)-y(x))/h
    print("\nfd=", fd)
    print("h=", h, ">>", (fd-d)/d)
    func1.plot((np.log10(h), np.log10((fd-d)/d)))

for b in np.arange(0, 20, 1):
    h = .1**b
    cd = (y(x+h/2)-y(x-h/2))/h
    print("\ncd=", fd)
    print("h=", h, ">>", (cd-d)/d)
    func2.plot((np.log10(h), np.log10((cd-d)/d)))

for c in np.arange(0, 20, 1):
    h = .1**c
    ed = (8*(y(x+h/4)-y(x-h/4))-(y(x+h/2)-y(x-h/2)))/(3*h)
    print("\ned=", fd)
    print("h=", h, ">>", (ed-d)/d)
    func3.plot((np.log10(h), np.log10((ed-d)/d)))
