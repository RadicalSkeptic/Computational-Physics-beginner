from vpython import *
import random

import winsound

lambda1 = 0.005
max = 80
time_max = 500
seed = 68111
number = nloop = max
graph1 = graph(title='Spontaneous Decay', xtitle='time', ytitle='number')
decayfunc = gcurve(color=color.green)

for time in arange(0, time_max+1):
    for atom in arange(0, number+1):
        decay = random.random()
        if(decay < lambda1):
            nloop = nloop-1
            winsound.Beep(600, 100)
    number = nloop
    decayfunc.plot(pos=(time, number))
    rate(30)
