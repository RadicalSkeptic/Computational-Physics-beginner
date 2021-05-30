from vpython import *

y = .5
m = 3.99

graph1 = graph(title="population", xmin=0, xmax=100, scroll=True,  fast=False)
pts = gcurve(color=color.green)
n = 0
while n < 1000:
    pts.plot(n, y)
    y = y*m*(1-y)
    n += 1
    rate(30)
