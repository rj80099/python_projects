from turtle import Turtle,Screen
import random
screen=Screen()
screen.setup(500,400)

#tim.shape('turtle')
colors=['red','green','blue','yellow','orange','purple']
user_bet=screen.textinput("Which clolor you want to bet?",'')
new_pos=-70
racers=[]
for index in range(0,6):
    tim = Turtle(shape='turtle')
    tim.color(colors[index])
    tim.penup()
    new_pos+=30
    tim.goto(x=-230,y=new_pos)
    racers.append(tim)


is_race_on=True
while is_race_on:
    for tur in racers:
        tur.forward(random.randint(0, 10))

        if(tur.xcor()>=240):
            if(user_bet==tur.pencolor()):
                print(f"your {tur.pencolor()} turtle won")
            else:
                print(f"your {tur.pencolor()} turtle loss")
            is_race_on=False


screen.exitonclick()