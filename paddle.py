from turtle import Turtle

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.color("deep pink")
        self.shape("square")

        self.shapesize(1, 6)
        self.penup()
        self.goto(0, -250)

    def left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    def right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())
