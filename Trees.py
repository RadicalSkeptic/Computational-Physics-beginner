from turtle import *
from numpy import *

length = 10
branch_len = 100
turn = 45
speed(0)
tracer(0, 0)


def branch_draw(i, direct, locat):
    pencolor('Brown')
    penup()
    setpos(locat)
    seth(direct)
    pendown()
    while i <= length:
        pensize(5-4*i/10)
        if i >= 3:
            pencolor('Green')
        forward(branch_len*(.8**i))
        right(random.uniform(-turn, turn))
        i += 1
        if random.random() <= .8:
            step.append(i)
            direction.append(heading())
            loc.append(pos())


def tree_draw():
    points = 0
    point = 0
    while point <= points:
        branch_draw(step[point], direction[point], loc[point])
        points = len(step)
        point += 1
        if point == points:
            break


for k in range(4):
    step = [0]
    direction = [90]
    loc = [[0, -200]]
    tree_draw()
    update()

done()
