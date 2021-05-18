import random
import numpy
import vpython

steps = 4250
x = 0
y = 0

list = numpy.array([1, 2, 3, 4])
graph1 = vpython.graph(title="random walk", width=1166, height=600)
func = vpython.gcurve(color=vpython.color.blue)
for i in numpy.arange(0, steps, 1):
    f = random.choice(list)
    func.plot(x, y)
    if (f == 1):
        x += 1
    elif(f == 2):
        y += 1
    elif(f == 3):
        x -= 1
    elif(f == 4):
        y -= 1
    else:
        print("ERROR!")
    vpython.rate(50)
