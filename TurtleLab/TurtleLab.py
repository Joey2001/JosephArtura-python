import turtle
from random import randint
width = 800
height = 800
turtle.setup(width = width, height = height)
turtle.bgcolor('white')
turtle.speed(0)
# num = int(input("What is your number"))
# w = int((num -2) * 360 / (num / 2))
# y = int((num - 2) * 360 / (num))
# try factors of 360
# def rectDraw():
#     pen.color("#afed12")
#     for x in range(num):
#         y = int((num - 2) * 360 / (num))
#         pen.left(y)

def spirl(angle):
    for i in range(1000):
        turtle.forward(i)
        turtle.left(angle)
def line(length, direction, color, e,f):
    moveT(e,f)
    turtle.pencolor(color)
    if direction == "up":
        turtle.left(90)
    elif direction == "down":
        turtle.left(-90)
    else:
        turtle.left(0)
    turtle.forward(length)

def basicRec(sides, length, width, e, f, color):
    moveT(e,f)
    turtle.pencolor(color)
    for x in range(sides):
        turtle.forward(length)
        turtle.left(360/sides)
        turtle.forward(width)
        turtle.left(360/sides)

def basicShape(sides, length, e, f, color, red, green, blue, hexRGB):
    moveT(e,f)
    if hexRGB:
        turtle.pencolor(color)
    else:
        turtle.pencolor(red, green, blue)
    for x in range(sides):
        turtle.forward(length)
        turtle.left(360/sides)
def circle(radius,color, e, f):
    turtle.color(color)
    moveT(e, f)
    turtle.circle(radius)

def moveT(x,y):
    turtle.penup()
    turtle.setpos(x, y)
    turtle.pendown()

basicShape(4, 100, 0, 0, input("What color?"), 0, 0, 0, True)
basicRec(4, 100, 50, -110, 110, "#ffffff")
basicShape(4, 100, 110, 110, input("What color?"), 0, 0, 0, True)
basicRec(4, 100, 50, -110, -110, "#554433")
basicRec(4, 0, 50, 0, -25, input("What color?"))
basicRec(4, 50, 0, -25, 0, "#554433")
basicShape(3, 100, -250, 250, "#ffffff", 0, 0, 0, True)
basicShape(4, 200, -100, -100, input("What color?"), 0, 0, 0, True)
def shapeInput():
    repeat = int(input("How many shapes do you want to draw?"))
    for i in range(repeat):
        sides = int(input("How many sides?"))
        length = int(input("How long is each side?"))
        xoff = int(input("what is the x offset?"))
        yoff = int(input("what is the y offset?"))
        color = input("What is the color?")
        basicShape(sides, length, xoff, yoff, color, 0, 0, 0, True)
# shapeInput()
circle(50, "black", 150, -150)
basicShape(3, 50, 150, 50, "red", 1, 1, 1, True)
basicShape(5, 50, -150, 50, "green", 1, 1, 1, True)
basicShape(9, 50, -150, -150, "blue", 1, 1, 1, True)
line(width, 'left', 'black', -(width/2), 0)
line(height, 'up', 'black', 0, -(height/2))

def circleTwo(radius):
    moveT(-50, 35)
    constant = 1
    i = 0
    colors = ['red', 'orange', 'green', 'blue', 'purple', 'magenta', 'cyan', 'black']
    for x in range(radius):
        red = randint(0,255)
        green = randint(0,255)
        blue = randint(0,255)
        #turtle.color(red / 255, green / 255, blue / 255)
        turtle.color(colors[i])
        turtle.circle(radius)
        turtle.left(50)
        i += 1
        if i >= len(colors):
            i = 0
        constant += 3
    for x in range(radius):
        red = randint(0,255)
        green = randint(0,255)
        blue = randint(0,255)
        turtle.color(red / 255, green / 255, blue / 255)
        #turtle.color(colors[i])
        turtle.circle(2 * radius)
        turtle.left(50)
        i += 1
        if i >= len(colors):
            i = 0
        constant += 3
circleTwo(75)

turtle.exitonclick()
