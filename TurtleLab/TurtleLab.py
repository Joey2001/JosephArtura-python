import turtle
pen = turtle.Pen()
turtle.setup(width = 800, height = 800)
turtle.bgcolor(input("Background color?"))
turtle.speed(0)
num = int(input("What is your number"))
# w = int((num -2) * 360 / (num / 2))
# y = int((num - 2) * 360 / (num))
# try factors of 360
def rectDraw():
    pen.color("#afed12")
    for x in range(num):
        y = int((num - 2) * 360 / (num))
        pen.left(y)
def rect():
    moveT(-300,300)
    pen.color("#afff34")
    for x in range(2):
        pen.forward(100)
        pen.left(90)
        pen.forward(50)
        pen.left(90)
def spirl(angle):
    for i in range(1000):
        pen.forward(i)
        pen.left(angle)

def square():
    turtle.pencolor("#aa00bc")
    for x in range(4):
        turtle.forward(100)
        turtle.left(90)
def basicRec(sides, length, width, e, f, color):
    moveT(e,f)
    turtle.pencolor(color)
    for x in range(2):
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

def moveT(x,y):
    turtle.penup()
    turtle.setpos(x, y)
    turtle.pendown()

#spirl(92)
rectDraw()
basicShape(4, 100, 0, 0, input("What color for this shape?"), 0, 0, 0, True)
basicRec(4, 100, 50, -110, 110, "#ffffff")
basicShape(4, 100, 110, 110, input("What color for this shape?"), 0, 0, 0, True)
basicRec(4, 100, 50, -110, -110, "#554433")
basicRec(4, 0, 50, 0, -25, input("What color for this shape?"))
basicRec(4, 50, 0, -25, 0, "#554433")
basicShape(3, 100, -250, 250, "#ffffff", 0, 0, 0, True)
basicShape(4, 200, -100, -100, input("What color for this shape?"), 0, 0, 0, True)
moveT(0, -300)
turtle.circle(300)
basicShape(3, 400, -200, -163, "#ffffff", 1, 1, 1, False)


turtle.exitonclick()
