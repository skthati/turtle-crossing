from turtle import Turtle

class Player(Turtle):
    def __init__(self) :
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.goto(0, -300)
        self.left(90)
        self.p_speed = 0.1

        self.px = 0
        self.py = 10
    
    def move(self):
        new_y = self.ycor() + self.py
        self.goto(self.px, new_y)
    
    def goto_start(self):
            self.goto(self.px, -300)