
# Challenge 1 and 2
# import random
# from turtle import Turtle
#
# tim = Turtle()
# tim.shape("turtle")
# tim.color("red")

#tim = colormode(255)


# for x in range(0, 4):
#
#   tim.forward(100)
#   tim.right(90)



# def dashed_line(length):
#   while range(length):
#     tim.pendown()
#     tim.forward(5)
#     tim.penup()
#     tim.forward(5)
#
#
# dashed_line(100)

# Drawing multiple quadrilateral
# color = ["red", "green", "blue", "cyan", "magenta", "yellow", "pink", "gray", "black", "white"]
#
# from random import choice
# def draw_quad(sides):
#   for i in range(3,sides+1):
#     tim.color(random.choice(color))
#     tim.setheading(0)
#     for j in range(0,i):
#       tim.pendown()
#       tim.forward(50)
#       tim.right(360/i)
#
# draw_quad(7)


# random walk

from random import choice
direction = [0,90,180,270]
# color = ["red", "green", "blue", "cyan", "magenta", "yellow", "pink", "gray", "black", ]

# def random_walk(walk):
#   tim.pen(speed = 10)
#   tim.pendown()
#   tim.width(15)
#   step = 0
#   while step <= walk:
#     tim.color(random.choice(color))
#     tim.setheading(random.choice(direction))
#     tim.forward(30)
#     step += 1


# random_walk(100)

# Challenge 3 random color

import random
import turtle as t

tim = t.Turtle()
#tim.shape("turtle")
t.colormode(255)

def random_color():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  random_color = (r, g, b)
  return random_color

def random_walk(walk):
  tim.pen(speed = 10)
  tim.pendown()
  tim.width(15)
  step = 0
  while step <= walk:
    tim.color(random_color())
    tim.setheading(random.choice(direction))
    tim.forward(30)
    step += 1

random_walk(100)


screen  = Screen()
screen.exitonclick()