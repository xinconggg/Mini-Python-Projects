from turtle import *
import random

# Initialize Screen size to 500x400
screen = Screen()
screen.setup(width=500, height=400)
is_race_on : False

# Prompt user to bet
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ".lower())

# Set list of colors and y-positions
colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange']
y_positions = [-100, -60, -20, 20, 60, 100]
all_turtles = []

# Set turtle's initial position
for i in range(6):
    t = Turtle(shape="turtle")
    t.color(colors[i])
    t.penup()
    t.goto(x=-230, y=y_positions[i])
    all_turtles.append(t)

# Start Race
if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        # Stop Race when a turtle crosses the winning line and determine the winner
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've Won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've Lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)



screen.exitonclick()