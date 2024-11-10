import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super(CarManager, self).__init__()
        self.allcars = []
        self.carspeed = STARTING_MOVE_DISTANCE

    def create_car(self):
        new_car = Turtle()
        new_car.shape("square")
        new_car.shapesize(stretch_wid = 2, stretch_len = 1)
        #new_car.penup()
        new_car.color(random.choice(COLORS))
        new_y = random.randint(-250, 250)
        new_car.goto(300, new_y)
        self.allcars.append(new_car)


