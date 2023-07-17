# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('dots.jpg', 20)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

from turtle import *
import random


colors_list = ['#07122d', '#9a2a72', '#a55447', '#761d53', '#df7ab7', '#7bb4ce', '#0593c1', '#858382', '#dbadc7',
               '#ac6083', '#2799bf', '#b66258', '#9ecbda', '#ddb1ab', '#611839', '#7f7e88']

t = Turtle()


def hirst_spot_painting():
    t.speed('fastest')
    t.penup()
    t.setheading(225)
    t.forward(325)
    t.setheading(0)
    for _ in range(5):
        for _ in range(10):
            t.dot(20, random.choice(colors_list))
            t.forward(50)
        t.left(90)
        t.forward(50)
        t.left(90)
        t.forward(50)
        for _ in range(10):
            t.dot(20, random.choice(colors_list))
            t.forward(50)
        t.right(90)
        t.forward(50)
        t.right(90)
        t.forward(50)


hirst_spot_painting()


screen = Screen()
screen.exitonclick()
