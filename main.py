# Case 2
# Developers:
# - Simonova Tanya
# - Novikov Dmitriy
# - Churina Margaery

import turtle
import math

def trian(x, y, side1, side2, side3, angle_of_rotation, color):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.color(color)
    turtle.begin_fill()
    turtle.right(angle_of_rotation)
    turtle.forward(side1)
    turtle.right(180 - math.degrees(math.acos(
        (side1 ** 2 + side2 ** 2 - side3 ** 2) / 2 / side1 / side2)))
    turtle.forward(side2)
    turtle.right(180 - math.degrees(math.acos(
        (side2 ** 2 + side3 ** 2 - side1 ** 2) / 2 / side2 / side3)))
    turtle.forward(side3)
    turtle.right(180 - math.degrees(math.acos(
        (side3 ** 2 + side1 ** 2 - side2 ** 2) / 2 / side3 / side1)))
    turtle.end_fill()


def rect(x, y, side1, side2, angle_of_rotation, color):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.color(color)
    turtle.begin_fill()
    turtle.right(angle_of_rotation)
    for _ in range(2):
        turtle.forward(side1)
        turtle.right(90)
        turtle.forward(side2)
        turtle.right(90)
    turtle.end_fill()


def circ(x, y, side, color):
    x_1 = x - side
    y_1 = y - side
    turtle.up()
    turtle.goto(x_1, y_1)
    turtle.down()
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(side)
    turtle.end_fill()


def square(x, y, side, angle_of_rotation, color):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.color(color)
    turtle.begin_fill()
    turtle.right(angle_of_rotation)
    for _ in range(4):
        turtle.forward(side)
        turtle.right(90)
    turtle.end_fill()


def rhom(x, y, side, angle, angle_of_rotation, color):
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.right(angle_of_rotation)
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(side)
        turtle.right(180 - angle)
        turtle.forward(side)
        turtle.right(angle)
    turtle.end_fill()


def trap(x, y, bigger_base, side, angle, angle_of_rotation, color):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.color(color)
    turtle.begin_fill()
    turtle.right(angle_of_rotation)
    turtle.forward(bigger_base)
    turtle.left(180 - angle)
    turtle.forward(side)
    turtle.left(angle)
    turtle.forward(bigger_base - 2 * math.cos(math.radians(angle))*side)
    turtle.left(angle)
    turtle.forward(side)
    turtle.end_fill()


turtle.speed(50000)

# картинки

turtle.bgcolor("lightcyan")

# корабль (Дима)
trap(-300, -300, 300, 100, 60, 180, "darkblue")
circ(-475, -325, 20, "deepskyblue")
circ(-425, -325, 10, "deepskyblue")
circ(-395, -325, 10, "deepskyblue")
rect(-350, -300, 200, 5, -30, "saddlebrown")
trian(-345, -100, 100, 60, 80, 180 - math.degrees(math.acos(
    (40 ** 2 + 50 ** 2 - 30 ** 2) / 2 / 50 / 40)), "orangered")
rect(-475, -300, 100, 5, 180 + math.degrees(math.acos(
    (40 ** 2 + 50 ** 2 - 30 ** 2) / 2 / 50 / 40)), "saddlebrown")
trian(-470, -200, 50, 30, 40, 180 - math.degrees(math.acos(
    (40 ** 2 + 50 ** 2 - 30 ** 2) / 2 / 50 / 40)), "orangered")
turtle.right(math.degrees(math.acos((40 ** 2 + 50 ** 2 - 30 ** 2) / 2 / 50 / 40)))

# конфета (Дима)
circ(100,300,40,"lightseagreen")
trian(110, 300, 60, 60, 60, -50, "mediumpurple")
rect(110, 300, 55, 0.5, 10, "indigo")
rect(110, 300, 52.5, 0.5, 10, "indigo")
rect(110, 300, 51, 0.5, 10, "indigo")
rect(110, 300, 52.5, 0.5, 10, "indigo")
rect(110, 300, 55, 0.5, 10, "indigo")
turtle.left(50)
trian(30, 300, 60, 60, 60, 190, "mediumpurple")
rect(30, 300, 55, 0.5, 10, "indigo")
rect(30, 300, 52.5, 0.5, 10, "indigo")
rect(30, 300, 51, 0.5, 10, "indigo")
rect(30, 300, 52.5, 0.5, 10, "indigo")
rect(30, 300, 55, 0.5, 10, "indigo")
circ(122, 365, 35, "khaki")
turtle.right(105)

turtle.done()

