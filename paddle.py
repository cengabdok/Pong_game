from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.turtlesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.speed('fastest')
        self.goto(position)

    def go_up(self):
        new_y = self.ycor()+30
        self.goto(self.xcor(),new_y)

    def go_down(self):
        new_y = self.ycor()-30
        self.goto(self.xcor(),new_y)