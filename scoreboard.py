from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")
LIVES = "💗💗💗💗💗"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.lives = LIVES
        self.penup()
        self.hideturtle()
        self.color("White")
        self.setposition(x=0, y=270)
        self.score = 0
        with open("highscore.txt", mode="w") as file:
            file.write("0")
        with open("highscore.txt") as file:
            self.high_score = int(file.read())

        self.update_score()

    def update_score(self):
        """Update the scoreboard"""
        self.clear()
        self.write(f"Lives: {self.lives} Score: {self.score} High Score: {self.high_score}", False, ALIGNMENT, FONT)

    def game_over(self):
        """Print GAME OVER on the screen"""
        self.goto(0, 0)
        self.write("GAME OVER", False, ALIGNMENT, ("Courier", 35, "bold"))

    def increase_score(self, color):
        """Increase the score by 1, 3, 5 or 7 depending on the color of the brick"""
        if color == "green":
            self.score += 1
        if color == "yellow":
            self.score += 3
        if color == "orange":
            self.score += 5
        if color == "red":
            self.score += 7
        self.update_score()

    def remove_life(self):
        """Remove a life from the scoreboard"""
        global LIVES
        self.lives = self.lives[:-1]
        self.update_score()

    def check_highscore(self):
        """Check if the current score is higher than the high score"""
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscore.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.update_score()
