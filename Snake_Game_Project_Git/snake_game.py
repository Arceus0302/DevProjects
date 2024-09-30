from turtle import Screen
from scoreboard import ScoreBoard
from snake import Snake
from food import Food
import time
#set the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

#calling the classes from the other .py files
snake = Snake()
food = Food()
scoreboard = ScoreBoard()
#setting the control key for game.
screen.listen()
screen.onkey(snake.up ,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

#program which animates the snake game.
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() >285 or snake.head.xcor() < -285 or snake.head.ycor() >285 or snake.head.ycor() < -285:
        scoreboard.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
