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


# картинки

def house(f1, f2):
    pass # (Симон)
    pass  # (Симон)


def fish(f1, f2):
    pass # (Симон)
    pass  # (Симон)


# кораблик
trap(-300, -300, 300, 100, 60, 180, "blue")
circ(-475, -325, 20, "white")
circ(-425, -325, 10, "white")
circ(-395, -325, 10, "white")
rect(-350, -300, 200, 5, -30, "brown")
trian(-345, -100, 100, 60, 80, 180 - math.degrees(math.acos(
    (40 ** 2 + 50 ** 2 - 30 ** 2) / 2 / 50 / 40)), "green")
rect(-475, -300, 100, 5, 180 + math.degrees(math.acos(
    (40 ** 2 + 50 ** 2 - 30 ** 2) / 2 / 50 / 40)), "brown")
trian(-470, -200, 50, 30, 40, 180 - math.degrees(math.acos(
    (40 ** 2 + 50 ** 2 - 30 ** 2) / 2 / 50 / 40)), "yellow")
turtle.left(math.degrees(math.acos((40 ** 2 + 50 ** 2 - 30 ** 2) / 2 / 50 / 40)))


# гусеница
x = -100
for _ in range(4):
    circ(x,300,40,"green")
    x += 80
circ(215,330,40,"green")
rhom(205,375,20,60,135,"black")
rhom(160,375,20,60,160,"black")

# дерево
circ(0, 0, 50, "green")
circ(-72, 30, 5, "red")
circ(-66, -10, 5, "red")
circ(-49, -3, 5, "red")
circ(-80, -20, 5, "red")
circ(-98, 3, 5, "red")
rect(-80, -65, 150, 10, 140, "brown")

# корона
rect(150, 0, 40, 100, 0, "yellow")
trian(150, 0, 35, 20, 20, 90, "red")
trian(120, 0, 35, 20, 20, 0, "green")
trian(90, 0, 35, 20, 20, 360, "blue")
circ(110, - 10, 5, "red")
