from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("deep sky blue")
        self.x_move = 1.5
        self.y_move = 1.5
        self.move_speed = 0.0001
        self.goto(10, -220)

    def move(self):
        """Move the ball"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_back_y(self):
        self.y_move *= -1

    def bounce_back_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(10, -220)
        self.bounce_back_y()
        self.move_speed = 0.0001
