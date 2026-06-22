import turtle
from turtle import Turtle
import pandas

# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# screen.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
t = Turtle()
turtle.shape(image)
t.hideturtle()

score = 0
data = pandas.read_csv("50_states.csv")
t.penup()
guessed_states = []
while score != 50:
    answer_state = screen.textinput(title=f"Guess the state {score}/50 ", prompt="What's another state's name?")
    if answer_state is None:
        break
    answer_state = answer_state.title()
    if answer_state == "Exit":
        missing_states = [state for state in data.state.to_list() if state not in guessed_states]
        data_learn = pandas.DataFrame(missing_states)
        data_learn.to_csv("States_to_learn.csv")
        break
    elif answer_state in data.state.to_list() and answer_state not in guessed_states:
        guessed_state = data[data.state == answer_state]
        x = guessed_state["x"].item()
        y = guessed_state["y"].item()
        t.goto(x,y)
        t.pendown()
        t.write(answer_state)
        t.penup()
        score += 1
        guessed_states.append(answer_state)
screen.exitonclick()