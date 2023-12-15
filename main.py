from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title("Pong by Ribz")
screen.tracer(0)

paddle1 = Paddle(350, 0)
paddle2 = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle1.move_up, 'Up')
screen.onkey(paddle1.move_down, 'Down')
screen.onkey(paddle2.move_up, 'w')
screen.onkey(paddle2.move_down, 's')

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    # Detect Collision with the ball
    if ball.ycor() > 280 or ball.ycor() < - 280:
        ball.bounce_wall()

    # Detect Collision with paddle 1 & 2
    if ball.distance(paddle1) < 50 and ball.xcor() > 320 or ball.distance(paddle2) < 50 and ball.xcor() < -320:
        ball.bounce_paddle()

    # Detect ball missing paddle 1
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.paddle2_point()

    # Detect ball missing paddle 2
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.paddle1_point()

screen.exitonclick()
