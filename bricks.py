from turtle import Turtle

colors = ["red", "orange", "yellow", "green"]


class Bricks(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.all_bricks = []
        self.all_stamps = []
        self.create_all()

    def create_all(self):
        """Create all the bricks"""
        y_position = 200
        for color in colors:
            for _ in range(2):
                self.create_bricks(y_position, color)
                y_position -= 25

    def create_bricks(self, y_position, color):
        """Create a row of bricks"""
        color = colors.index(color)

        for j in range(16):
            new_brick = Turtle("square")  # create a new brick iterating on j
            new_brick.shapesize(stretch_wid=1, stretch_len=2)
            new_brick.color(colors[color])  # color the brick with the item of the list colors
            new_brick.penup()
            new_brick.goto(-350 + j*45, y_position)  # position the brick (j*50 is the distance between bricks)
            # 0*50 is the first brick, 1*50 is the second brick, etc.
            stamp_id = new_brick.stamp()
            # print(stamp_id)
            self.all_bricks.append(new_brick)
            self.all_stamps.append(stamp_id)
        # print(len(self.all_bricks))

    def remove_brick(self, brick):
        """Remove a brick from the screen"""
        index = self.all_bricks.index(brick)
        brick.clearstamp(self.all_stamps[index])  # clear the stamp of the brick
        brick.hideturtle()
        self.all_bricks.remove(brick)
        self.all_stamps.remove(self.all_stamps[index])  # remove the stamp id from the list

    def get_brick_color(self, brick):
        """Get the color of the brick"""
        index = self.all_bricks.index(brick)
        return self.all_bricks[index].color()[0]





