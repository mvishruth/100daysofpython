




class PrintDots:


  def __init__(self, no_of_dots):

    import turtle
    def print_dots():
      t = turtle.Turtle
      for x in range(no_of_dots):
        t.color("black", "red")
        t.begin_fill()
        t.circle(10)
        t.end_fill()

class RandomColor


  def __init__(self, colors):
    import random
    color_palette = colors
    random_color = random.choice(color_palette)
    return random_color