import random
from turtle import Turtle, Screen

colors_list = [(237, 242, 238), (238, 239, 243), (240, 241, 234), (168, 89, 29), (240, 226, 73), (208, 88, 138),
               (135, 54, 97), (242, 232, 237), (20, 28, 55), (37, 49, 112), (46, 88, 161), (130, 33, 42), (153, 23, 16),
               (47, 35, 27), (103, 158, 223), (89, 89, 32), (52, 33, 40), (149, 211, 190), (31, 38, 28),
               (195, 161, 115), (197, 127, 162), (222, 88, 40), (251, 225, 2), (85, 90, 194), (158, 202, 222),
               (151, 195, 180), (221, 173, 190), (156, 130, 83), (170, 190, 220), (228, 175, 165)]

screen = Screen()
screen.colormode(255)
tim = Turtle()
tim.shape("circle")
tim.pensize(20)
tim.penup()
tim.hideturtle()


def square_dot_painting():
    tim.clear()
    x = -200
    y = -200
    tim.setposition(x, y)
    for i in range(10):
        for k in range(10):
            tim.dot(20, random.choice(colors_list))
            tim.forward(50)
        y += 40
        tim.setposition(x, y)


def triangle_dot_painting():
    tim.clear()
    x = -200
    y = -200
    tim.setposition(x, y)
    for i in range(10, 0, -1):
        for k in range(i):
            tim.dot(20, random.choice(colors_list))
            tim.forward(50)
        x += 25
        y += 40
        tim.setposition(x, y)


triangle_dot_painting()
square_dot_painting()
screen.exitonclick()
