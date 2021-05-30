from vpython import *

m_min = 3.5
m_max = 4
step = .0005

graph1 = graph(title="logistics map",  fast=False)
pts = gdots(radius=.1, color=color.green)
lasty = int(1000*.5)
count = 0
for m in arange(m_min, m_max, step):
    y = .05
    for i in range(1, 201, 1):
        y = m*y*(1-y)
    for i in range(201, 402, 1):
        y = m*y*(1-y)
    for i in range(201, 402, 1):
        oldy = int(1000*y)
        y = m*y*(1-y)
        inty = int(1000*y)
        if inty != lasty and count % 2 == 0:
            pts.plot(m, y)
        lasty = inty
        count += 1
