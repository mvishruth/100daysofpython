from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()




def move_forward():
  tim.forward(10)

screen.listen()
screen.onkey(key = "space", fun = move_forward)

screen.exitonclick()


# # Example Calculator function inside function
#
# def add(n1, n2):
#   return n1 + n2
#
# def subtraction(n1, n2):
#   return n1 - n2
#
# def multiply(n1, n2):
#   return n1 * n2
#
# def divide(n1, n2):
#   return n1 / n2
#
# def calculator(n1, n2, func):
#   return func(n1, n2)
#
# result = calculator(2, 3, multiply)
# print(result)