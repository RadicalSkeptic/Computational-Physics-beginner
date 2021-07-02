import turtle


def body(x, y):
    w = turtle.Turtle()
    w.shape('circle')
    w.color('white')
    w.speed(0)
    w.penup()
    w.goto(x, y)
    w.pendown()
    return w


a = body(0, 0)
b = body(100, 100)
obj = [a, b]

for i in obj:
    print(i)
