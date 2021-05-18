import numpy as p
from vpython import *

plot1 = gcurve(color=color.black)
for x in arange(0, 50, .05):
    plot1.plot(pos=(x, sin(x)/x))
