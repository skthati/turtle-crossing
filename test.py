from turtle import Turtle, Screen

sc = Screen()
t = Turtle()

t.shape("turtle")
for _ in range(3):
    t.forward(10)
    t.right(90)
t.pencolor("blue")
t.forward(50)

sc.exitonclick()