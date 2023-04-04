from turtle import Turtle
import random

# scb = Scoreboard()


class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(180)
        self.color_lst = ["red", "blue", "pink", "green", "brown"]
        self.color(random.choice(self.color_lst))
        self.dy = random.randint(-250, 250)
        self.goto(350, self.dy)
        self.x_speed = 10
        self.traffic_speed = 0.1
    
    def move(self):
        new_x = self.xcor() - 10
        self.goto(new_x, self.ycor())
    
    def increase_traffic_speed(self):
        self.traffic_speed *= 0.5
    
    def reset_traffic_speed(self):
        self.traffic_speed = 0.1
        
    

