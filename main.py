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

x = 0
# Game loop
game_start = True
while game_start:
    sc.update()
    

    # player crossing
    player.move()

    # Check end of crossing
    if player.ycor() == 300:
        player.goto_start()
    
    if x % 5 == 0:
        # Generate cars
        c1 = Cars()
    
    c1.move()

    x += 1
    

    time.sleep(player.p_speed)


sc.exitonclick()