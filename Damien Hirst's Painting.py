# import colorgram

# # Extract 20 colors from the image
# colors = colorgram.extract('image.jpg', 20)

# rgb_colors = []
# for i in colors:
#     red = i.rgb.r
#     green = i.rgb.g
#     blue = i.rgb.b
#     new_color = (red, green, blue)
#     rgb_colors.append(new_color)
# print(rgb_colors)

import turtle
import random

# Use the commands above to get a list of colors from the given image
color_list = [(198, 13, 32), (248, 236, 25), (40, 76, 188), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62)]

turtle.colormode(255)
t = turtle.Turtle()
t.speed("fastest")
t.penup()
t.hideturtle()

t.setheading(225)
t.forward(300)
t.setheading(0)
number_of_dots = 100

for i in range(1, number_of_dots + 1):
    random_color = random.choice(color_list)
    t.dot(20, random_color)
    t.forward(50)

    if i % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)

screen = turtle.Screen()
screen.exitonclick()