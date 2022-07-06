
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import turtle
import pandas

screen =turtle.Screen()
# player=turtle.Turtle()
screen.title("U.S. States Game")
screen.setup(width=725,height=491)
image ="blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
data=pandas.read_csv("50_states.csv")
states=data["state"].to_list()
guessed_state=[]
while len(guessed_state)<3:
    user_input =screen.textinput(f"{len(guessed_state)}/50 State_Correct","What's another state name?")
    if user_input=="exit":
    #     missing_states=[]
    #     for state in states:
    #         if state not in guessed_state:
    #             missing_states.append(state)
    #using list comrehension
        missing_states=[state for state in states if state not in guessed_state]
        new_data=pandas.DataFrame(missing_states)
        new_data.to_csv("state_to_learn.csv")
        break

    if user_input in states:
        if user_input not in guessed_state:
            t=turtle.Turtle()
            t.color("red")
            t.penup()
            t.hideturtle()
            state_data=data[data.state==user_input]
            t.goto(int(state_data.x),int(state_data.y))
            t.write(user_input, align="center", font=("Arail", 10, "normal"))
            guessed_state.append(user_input)


        #print(user_input)
        # print(states.)
         # data.drop(data["user_input"].index)





