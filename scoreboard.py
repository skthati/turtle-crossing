from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.pencolor("black")
        self.goto(0, 280)
        self.hideturtle()
        self.p_score = 0
        self.h_score = 0
        self.p_speed = 1
        self.write(f"Highest Score: {self.h_score}, Score: {self.p_score}, Speed: {self.p_speed}", align="center", font=("Arial", 40, "normal"))
    
    def increase_score(self):
        self.p_score += 1
        self.clear()
        self.write(f"Highest Score: {self.h_score}, Score: {self.p_score}, Speed: {self.p_speed}", align="center", font=("Arial", 40, "normal"))
    
    def increase_speed(self):
        self.p_speed += 1
        self.clear()
        self.write(f"Highest Score: {self.h_score}, Score: {self.p_score}, Speed: {self.p_speed}", align="center", font=("Arial", 40, "normal"))
    

    def reset_score(self):
        if self.h_score < self.p_score:
            self.h_score = self.p_score
        self.p_score = 0
        self.p_speed = 1
        self.clear()
        self.write(f"Highest Score: {self.h_score}, Score: {self.p_score}, Speed: {self.p_speed}", align="center", font=("Arial", 40, "normal"))


    