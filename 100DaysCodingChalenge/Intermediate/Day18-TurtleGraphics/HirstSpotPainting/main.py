# import colorgram
# rgb_color=[]
# colors=colorgram.extract('image.jpg',30)
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     new_color=(r,b,g)
#     rgb_color.append(new_color)
#
# print(rgb_color)

import turtle as turtle_module
import random

turtle_module.colormode(255)
tim=turtle_module.Turtle()
tim.hideturtle()
color_list=[ (200, 110, 167), (237, 246, 241), (144, 52, 74), (169, 45, 152), (58, 119, 92), (224, 131, 203), (136, 180, 162), (131, 26, 34), (51, 89, 117), (199, 72, 94), (143, 30, 25), (18, 74, 97), (69, 40, 47), (173, 153, 146), (150, 152, 177), (131, 74, 70), (56, 46, 43), (237, 163, 174), (184, 94, 88), (38, 71, 58), (28, 89, 82), (182, 178, 204), (242, 160, 156), (93, 124, 144), (20, 57, 66), (36, 96, 65), (108, 154, 125)]

#we need to move the turtule down to so as to print the dot in a rectangle
#for this we need to move the down at an angle of 225 degree and then move forward
tim.speed("fastest")
tim.penup()

tim.setheading(225)
tim.forward(300)
tim.setheading(0)

number_of_dots=100

for dot_count in range(1,number_of_dots+1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)
    if dot_count%10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen =turtle_module.Screen()
screen.exitonclick()
