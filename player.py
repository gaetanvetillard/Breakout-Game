from turtle import *

x=0
Y=-260
STARTING_POSITION = (x, Y)

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.setheading(90)
        self.shape("square")
        self.shapesize(stretch_len=0.5, stretch_wid=5)
        self.penup()
        self.color("white")
        self.goto(STARTING_POSITION)

    def go_left(self):
        x = self.xcor() - 20
        self.goto((x,Y))

    def go_right(self):
        x = self.xcor() + 20
        self.goto((x,Y))