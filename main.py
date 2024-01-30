from turtle import Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
from bricks import Bricks
import time
import winsound

screen = Screen()

screen.setup(width=820, height=600)
screen.bgcolor("black")
screen.title("THE BREAK_ADM GAME")
screen.tracer(0)

scoreboard = Scoreboard()  # preso da scoreboard.py
paddle = Paddle()  # preso da paddle.py
ball = Ball()  # preso da ball.py
bricks = Bricks()  # preso da bricks.py
def play():
    try:
        winsound.PlaySound("music.wav", winsound.SND_ASYNC | winsound.SND_LOOP)
    except Exception as e:
        print(f"Failed to play sound: {e}")

screen.listen()
screen.onkeypress(paddle.left, "Left")
screen.onkeypress(paddle.right, "Right")

game_is_on = True
hits = 0

# play music
play()

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 250:
        ball.bounce_back_y()
    if ball.xcor() > 335 or ball.xcor() < -360:
        ball.bounce_back_x()
    # Detect collision with paddle
    if ball.distance(paddle) < 50 and ball.ycor() < -230:
        ball.bounce_back_y()
        ball.bounce_back_x()
    # Detect collision with bricks
    for brick in bricks.all_bricks:
        if ball.distance(brick) < 25:
            ball.bounce_back_y()
            hits += 1
            print(hits)
            if hits % 5 == 0:
                ball.move_speed *= 0.2
            brick_color = bricks.get_brick_color(brick)
            print(brick_color)
            scoreboard.increase_score(color=brick_color)
            scoreboard.check_highscore()
            bricks.remove_brick(brick)
    # Detect paddle misses
    if ball.ycor() < -260:
        ball.reset_position()
        scoreboard.remove_life()
        print(scoreboard.lives)
        if scoreboard.lives == "":
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()
