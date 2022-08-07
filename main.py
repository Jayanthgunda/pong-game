from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.title("PING PONG")
screen.tracer(0)

l_paddle = Paddle((-380, 0))
r_paddle = Paddle((370, 0))
screen.setup(width=800, height=600)
screen.onkey(fun=l_paddle.up, key="Up")
screen.onkey(fun=l_paddle.down, key="Down")
screen.onkey(fun=r_paddle.up, key="Left")
screen.onkey(fun=r_paddle.down, key="Right")

screen.listen()
ball = Ball()
score_board = ScoreBoard()
game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 350 or ball.distance(l_paddle) < 50 and ball.xcor() < -350:
        ball.bounce_x()
        ball.move_speed *= 0.9

    if ball.xcor() > 400:
        ball.setposition(0, 0)
        ball.bounce_x()
        score_board.increase_left()
        ball.move_speed = 0.1

    if ball.xcor() < -400:
        ball.setposition(0, 0)
        ball.bounce_x()
        score_board.increase_right()
        ball.move_speed = 0.1


screen.exitonclick()
