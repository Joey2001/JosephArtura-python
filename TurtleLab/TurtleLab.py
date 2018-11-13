import turtle
pen = turtle.Pen()
turtle.bgcolor("#ff00ff")
turtle.speed(0)
def rectDraw():
    pen.color("#afed12")
    for x in range(2):
        pen.forward(100)
        pen.left(90)
        pen.forward(50)
        pen.left(90)
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
def circle():
    moveT(-150, 150)
    turtle.pencolor("#ce06ba")
    for x in range(75):
        turtle.forward(5)
        turtle.right(5)
    moveT(-210, 165)

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
# spirl(92)
# basicShape(4, 100, 0, 0, "#aaaaaa")
# basicRec(4, 100, 50, -110, 110, "#ffffff")
# basicShape(4, 100, 110, 110, "#adef34")
# basicRec(4, 100, 50, -110, -110, "#554433")
# basicShape(3, 100, -250, 250, "#ffffff")
basicShape(4, 200, -100, -100, "#aaaaaa", 0, 0, 0, True)
moveT(0, -300)
turtle.circle(300)
basicShape(3, 400, -200, -163, "#ffffff", 1, 1, 1, False)


turtle.setup(width = 700, height = 700)
turtle.bgcolor("#ff00ff")
turtle.speed(0)
turtle.exitonclick()
