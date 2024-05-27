from turtle import *

t = Turtle()
screen = Screen()

def forward():
    t.forward(10)

def backwards():
    t.left(40)
    t.left(40)
    t.forward(10)

def counter_clockwise():
    t.left(40)

def clockwise():
    t.right(40)

def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

screen.listen()

# Movements
screen.onkey(forward, "w")
screen.onkey(backwards, "s")
screen.onkey(counter_clockwise, "a")
screen.onkey(clockwise, "d")
screen.onkey(clear, "c")

screen.exitonclick()