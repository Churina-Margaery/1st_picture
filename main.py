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

# корона (Рита)
rect(-300, 400, 80, 210, 0, "gold")
trian(-300, 400, 70, 60, 60, 90, "gold")
trian(-370, 400, 70, 60, 60, 0, "gold")
trian(-440, 400, 70, 60, 60, 360, "gold")
rhom(-490, 380, 30, 60, 120, "tomato")
rhom(-350, 380, 30, 60, 0, "tomato")
rhom(-430, 380, 50, 60, 0, "royalblue")
turtle.right(76)

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

# дерево (Рита)
circ(100, -100, 50, "forestgreen")
circ(90, -110, 30, "forestgreen")
circ(70, -140, 30, "forestgreen")
circ(60, -120, 30, "forestgreen")
circ(40, -90, 30, "forestgreen")
circ(70, -70, 30, "forestgreen")
circ(80, -80, 30, "forestgreen")
circ(28, -70, 5, "red")
circ(34, -110, 5, "red")
circ(51, -103, 5, "red")
circ(20, -120, 5, "red")
circ(2, -97, 5, "red")
rect(20, -180, 150, 7, 139, "saddlebrown")
turtle.right(-90)

# дом (Таня)
square(350, 400, 120, 0, "navajowhite")
rect(370, 375, 55, 70, 0, "peru")
rect(375, 370, 20, 60, 0, "skyblue")
rect(400, 370, 20, 60, 0, "skyblue")
trap(325, 400, 170, 50, 50, 0, "crimson")
turtle.right(50)
rect(450, 438.3, 20, 40, 0, "dimgrey")
turtle.right(-180)

# рыба (Таня)
trap(300, -350, 180, 70, 45, 0, "cornflowerblue")
trap(480, -350, 180, 70, 45, 45, "cornflowerblue")
circ(520, -335, 49.5, "cornflowerblue")
trian(300, -350, 60, 90, 60, -184, "mediumorchid")
trian(400, -300.5, 30, 50, 40, 0, "darkmagenta")
trian(420, -390, 30, 60, 45, 240, "darkmagenta")
trian(370, -390, 30, 60, 45, 0, "darkmagenta")
circ(450, -330, 15, "white")
circ(450, -330, 5, "black")

turtle.done()

