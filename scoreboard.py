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
        self.username = ""
        self.write(f"Hi There {self.username}:      Highest Score: {self.h_score}, Score: {self.p_score}, Speed: {self.p_speed}", align="center", font=("Arial", 25, "normal"))
    
    def increase_score(self):
        self.p_score += 1
        self.clear()
        self.write(f"{self.username}:      Highest Score: {self.h_score}, Score: {self.p_score}, Speed: {self.p_speed}", align="center", font=("Arial", 25, "normal"))
    
    def increase_speed(self):
        self.p_speed += 1
        self.clear()
        self.write(f"{self.username}:      Highest Score: {self.h_score}, Score: {self.p_score}, Speed: {self.p_speed}", align="center", font=("Arial", 25, "normal"))
    
    def update_name(self):
        self.clear()
        self.write(f"Hello {self.username}:      Highest Score: {self.h_score}, Score: {self.p_score}, Speed: {self.p_speed}", align="center", font=("Arial", 25, "normal"))
    

    def reset_score(self):
        if self.h_score < self.p_score:
            self.h_score = self.p_score
        self.p_score = 0
        self.p_speed = 1
        self.clear()
        self.write(f"{self.username}:      Highest Score: {self.h_score}, Score: {self.p_score}, Speed: {self.p_speed}", align="center", font=("Arial", 25, "normal"))


    