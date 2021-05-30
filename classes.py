import turtle


class Polygon:
    def __init__(self, sides, name, size=100, color="black", line_thickness=1):
        self.sides = sides
        self.name = name
        self.size = size
        self.color = color
        self.line_thickness = line_thickness

    def draw(self):
        turtle.color(self.color)
        turtle.pensize(self.line_thickness)
        for i in range(self.sides):
            turtle.forward(self.size)
            turtle.right(360/self.sides)
        turtle.done()


class Square(Polygon):
    def __init__(self, size=100, color="Black", line_thickness=3):
        super().__init__(4, "Square", size, color, line_thickness)


square = Square(color="Green")
square.draw()
