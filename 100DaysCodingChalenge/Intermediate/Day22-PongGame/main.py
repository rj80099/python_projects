from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
import  time

screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor('black')
screen.title("Pong Game")
screen.listen()
screen.tracer(0) #disable starting animation
l_paddle=Paddle((-370,0))
r_paddle=Paddle((370,0))
ball=Ball()
scoreboard=Scoreboard()
screen.onkeypress(r_paddle.up,"Up")
screen.onkeypress(r_paddle.down,"Down")
screen.onkeypress(l_paddle.up,"w")
screen.onkeypress(l_paddle.down,"s")
game_is_on=True
while game_is_on:
  time.sleep(ball.move_speed)
  ball.move()
  screen.update()

  #Detect collision with wall
  if ball.ycor()>280 or ball.ycor()<-280:
    ball.bounce_y()

  #detecting collision with r_paddle paddle
  if ball.distance(r_paddle)<50 and ball.xcor()>340 or ball.distance(l_paddle)<50 and ball.xcor()<-340:
    ball.bounce_x()

  #detect R paddle misses
  if ball.xcor()>380:
    ball.reset_position()
    scoreboard.l_point()

  #detect L paddle misses
  if ball.xcor()<-380:
    ball.reset_position()
    scoreboard.r_point()





screen.exitonclick()

#game_is_on=True

#while game_is_on:
