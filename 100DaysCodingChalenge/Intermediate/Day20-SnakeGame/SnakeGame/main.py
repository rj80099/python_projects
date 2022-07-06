from turtle import Screen,Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


# Day 19 start
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

game_is_on =True
while game_is_on:
    time.sleep(.1)
    screen.update()
    snake.move()
    #Detect collision with food.
    #for this we will be distance method which is basically comparing two turtle distance.
    if snake.head.distance(food)<15:
        food.refresh()
        #update scoreboard
        snake.extend()
        scoreboard.increase_score()

    #detection collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
    #detection collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            scoreboard.reset()
            snake.reset()
    #if head collide with any segment in the tail
        #trigger game_over





#Day 19 ends









screen.exitonclick()