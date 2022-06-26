import turtle
from turtle import Turtle,Screen
#import turtle     This will only import the module
#from turtle import *   This will import everything that is there in  the module
#import turtle as t      Here we are using an alise for the turtle module
import random
tim =Turtle()
tim.shape("turtle")
tim.color("Red")
'''
#move the turtle such that a square is made
for _ in range(15):
    tim.forward(10)
    #dont draw any thing
    tim.penup()
    tim.forward(10)
    #start drawing again
    tim.pendown()

tim.left(90)

'''
#Draw different shape
#angle calculation:  360/num_side

'''
colours=["CornflowerBlue","DarkOrchid","IndianRed","DeepSkyBlue","LightSeaGreen","wheat","slateGray","SeaGreen"]
def draw_shape(num_sides):
    for _ in range(num_sides):
        angle=360/num_sides
        tim.forward(100)
        tim.right(angle)

for shape_size_n in range(3,11):
    tim.color(random.choice(colours))
    draw_shape(shape_size_n)
'''

'''
#Draw a random walk

turtle.colormode(255)

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color=(r,g,b)
    return random_color

#colours=["CornflowerBlue","DarkOrchid","IndianRed","DeepSkyBlue","LightSeaGreen","wheat","slateGray","SeaGreen"]
directions =[0,90,180,270]
tim.pensize(15)
tim.speed("fastest")   #0 for fastest
for _ in range(5):
    tim.forward(30)
    #tim.color(random.choice(colours))
    tim.color(random_color())
    tim.setheading(random.choice(directions))
'''
'''
#draw a sprial of radius 100

turtle.colormode(255)
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color=(r,g,b)
    return random_color

tim.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        current_heading=tim.heading()
        tim.setheading(current_heading+size_of_gap)

draw_spirograph(5)
'''













screen =Screen()
screen.exitonclick()