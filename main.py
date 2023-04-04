from turtle import Turtle, Screen
import time
from player import Player
from cars import Cars
import random


# Screen Setup
sc = Screen()
sc.setup(800, 650)

# Initiate Turtle
player = Player()

# Stop animation
sc.tracer(0)

# Random speed
def random_speed():
    return random.randint(1, 10)

# Traffic Turtles
traffic_turtles = []
x = 0
a = 5


# Game loop
game_start = True
while game_start:
    sc.update()
    

    # player crossing
    player.move()

    # Check end of crossing
    if player.ycor() == 300:
        player.goto_start()
    
    # Create new turtle on every 5th iteration
    if x % 10 == 0 and  x < 300:
        # Generate cars
        c1 = Cars()
        traffic_turtles.append(c1)

    
    for i in traffic_turtles:
        if i.distance(player) < 15:
            player.goto_start()
        

        if i.xcor() < -300:
            i.goto(300, i.ycor())
            i.move()
        else:
            i.move()

    x += 1

    
    

    time.sleep(player.p_speed)


sc.exitonclick()