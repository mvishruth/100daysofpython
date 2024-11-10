# import another_module
#
# print(another_module.another_variable)

# from turtle import Turtle, Screen
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
# print(timmy)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

#importing object
# import turtle
#
# timmy = turtle.Turtle()

# rewriting the same more neatly
# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# from turtle import *
# color('red', 'yellow')
# begin_fill()
# while True:
#   forward(200)
#   left(170)
#   if abs(pos()) < 1:
#     break
# end_fill()
# done()

# import sqlite3
# from prettytable import from_db_cursor
#
# connection = sqlite3.connect("mydb.db")
# cursor = connection.cursor()
# #cursor.execute("SELECT field1, field2, field3 FROM my_table")
# cursor.execute("SELECT field1, field2, field3 FROM my_table")
# mytable = from_db_cursor(cursor)


# from prettytable import PrettyTable
# table = PrettyTable()
# table.add_column("Pokemon", ["Pikachu", "Squirtle", "Wartole"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
# table.align = "l"
# print(table)
