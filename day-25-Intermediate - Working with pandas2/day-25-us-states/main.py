import turtle
import pandas
import os

screen = turtle.Screen()
screen.title("U.S. States Game")
# image = "/day-25-Intermediate - Working with pandas2/day-25-us-states/blank_states_img.gif"
# Get the current directory of the script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to the image
image = os.path.join(current_dir,"blank_states_img.gif")

screen.addshape(image)
turtle.shape(image)

#data = os.path.join(current_dir,"50_states.csv")
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States Correct.", prompt="What's another state's Name ?").title()
    print(answer_state)
    if answer_state == "Exit":
        missing_state = [state for state in all_states if state not in guessed_state]
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)



