from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score import Scoreboard
screen = Screen()
screen.setup(height=550, width=800)
screen.bgcolor("black")
screen.title("Anjali's Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
score = Scoreboard()




screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()


    # detect collision with the wall
    if ball.ycor() > 260 or ball.ycor() < -260:
        ball.bounce_y()

    # detect collision with the right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect when r_paddle misses
    if ball.xcor() > 380:
        ball.reset_pos()
        score.l_point()

    # detect when left paddle misses
    if ball.xcor() <-380:
        ball.reset_pos()
        score.r_point()



















screen.exitonclick()