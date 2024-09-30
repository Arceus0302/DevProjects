from turtle import  Screen
import time
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

#Created the screen and other foundation for the game.
screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.tracer(0)

r_paddle = Paddle((380 ,0))
l_paddle = Paddle((-380, 0)) #the left and right paddle of th game.
ball = Ball()
scoreboard = Scoreboard()
#control key to control both left and right paddle.
screen.listen()
screen.onkey(r_paddle.go_up , "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up , "w")
screen.onkey(l_paddle.go_down, "s")

#The main loop for the game to run.
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < - 340:
        ball.bounce_x()
    if ball.xcor() > 420 :
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor() < -420 :
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()