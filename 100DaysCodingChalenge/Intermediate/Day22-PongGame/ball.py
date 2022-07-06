
from turtle import Turtle


class Ball(Turtle):

    #Create a ball at the center of the window
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.move_x=10
        self.move_y=10
        self.move_speed=0.1

    #move the ball in increasing x and y cord
    def move(self):
        new_x=self.xcor()+self.move_x
        new_y=self.ycor()+self.move_y
        self.goto(new_x,new_y)
        self.move_speed=0.1

    def bounce_y(self):
        self.move_y*=-1

    def bounce_x(self):
        self.move_x*=-1
        self.move_speed*=.9
    def reset_position(self):
        self.goto(0,0)
        self.move_speed=0.1
        self.bounce_x()