import random

def myFunc(x,y):
    print(x)
    print(y)

i = 6
j = 10

def mySchool():
    print("I go to Bellarmine Prep and I like AP Computer Science A")

def calcGrade(grade):
    print("You have been in school for",grade,"years")

def City(city, year):
    print("You live in",city,"and you are in grade", year)

def Recieving(z):
    print(z)

def twoNumbers(a,b):
    print(random.randint(a,b))

def areaPlane(a,b):
    print("The box has an area of", (a*b), "units^2")

def Volume(a,b,c):
    print("The volume of the box is ",(a*b*c), "units^3")

areaPlane(float(input("What is the length? - ")), float(input("What is the width? - ")))
Volume(float(input("What is the length? - ")),float(input("What is the width? - ")),float(input("What is the height? - ")))
twoNumbers(float(input("What is your first number? - ")),float(input("What is your second number? - ")))
Recieving(input("What number?"))
myFunc(i,j)
mySchool()
calcGrade(int(input("What grade are you in? - ")))
City(input("What city do you live in? - ", int(input("What grade are you in? - "))))
