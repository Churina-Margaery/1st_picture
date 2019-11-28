# Case 2
# Developers:
# - Simonova Tanya
# - Novikov Dmitriy
# - Churina Margaery

import turtle
import math

def trian(x, y, side1, side2, side3, color):
    pass
  # Симон, тут ты пишешь функцию рисования треугольника с координатами (правый верхний угол) x, y, и сторонами side1, side2, side3

def rect(x, y, side1, side2, angle_of_rotation, color):
    pass
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
    turtle.forward(side)
    for _ in range(4):
        turtle.forward(side)
        turtle.right(90)
    turtle.end_fill()

def rhom(x, y, side, angle, angle_of_rotation, color):
    turtle.up()
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.color(color)
    turtle.right(360 - angle)
    turtle.left(angle)
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
    turtle.forward(bigger_base - 2*math.cos(math.radians(angle))*side)
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


def ship(f1, f2):
    pass # (Дима)
    pass  # (Дима)


def Catepilar(f1, f2, f3, f4, f5):
    pass # (Дима)
    pass  # (Дима)


def tree(f1, f2, f3):
    pass # (Я)
    pass  # (Я)


def tree_2(f1, f2):
    pass # (Я)
    pass  # (Я)
