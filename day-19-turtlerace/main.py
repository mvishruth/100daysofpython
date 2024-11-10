import random
from turtle import Turtle, Screen

screen = Screen()

screen.setup(width = 500, height = 400)
is_race_on = False
user_bet = screen.textinput(prompt="Enter a Color", title = "Which one are you betting on? " )
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
position = [-100, -60, -20, 20, 60, 100]
turtles = []


for x in range(0, 6):
  new_turtle = Turtle(shape="turtle")
  new_turtle.penup()
  new_turtle.goto(x = -230, y = position[x])
  new_turtle.color(colors[x])
  turtles.append(new_turtle)


if user_bet:
  is_race_on = True

while is_race_on:

  for turtle in turtles:
    if turtle.xcor() > 230:
      is_race_on = False
      if user_bet == turtle.pencolor():
        print(f"you have Won")
      else:
        print(f"You Lost, Winnning turtle is {turtle.pencolor()}")
    rand_distance = random.randint(0, 10)
    turtle.forward(rand_distance)









screen.listen()
screen.exitonclick()