from turtle import Turtle, Screen
import time
from player import Player
from cars import Cars
from scoreboard import Scoreboard
import random



# Screen Setup
sc = Screen()
sc.setup(800, 650)

# Initiate Turtle
player = Player()

# Initiate Scoreboard
pl_score = Scoreboard()

# Initiate Cars
c = Cars()

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
    time.sleep(c.traffic_speed)
    

    # player crossing
    player.move()

    # Check end of crossing
    if player.ycor() == 300:
        player.goto_start()
        pl_score.increase_score()
        pl_score.increase_speed()
        c.increase_traffic_speed()

    
    # Create new turtle on every 5th iteration
    if x % 10 == 0 and  x < 300:
        # Generate cars
        c1 = Cars()
        traffic_turtles.append(c1)

    
    for i in traffic_turtles:
        # Check traffic collision
        if i.distance(player) < 15:
            player.goto_start()
            c.reset_traffic_speed()
            pl_score.reset_score()
            x = 0
            for j in range(len(traffic_turtles)):
                traffic_turtles[j].hideturtle()
            
            traffic_turtles = []

        if i.xcor() < -300:
            i.goto(300, i.ycor())
            i.move()
        else:
            i.move()

    x += 1

    
    

    time.sleep(player.p_speed)


sc.exitonclick()