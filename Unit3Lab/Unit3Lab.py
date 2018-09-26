import random

def myFunc(x,y):
    print(x, y)

i = 6
j = 10

def mySchool():
    return "I go to Bellarmine Prep and I like AP Computer Science A"

def calcGrade(grade):
    return "You have been in school for",grade,"years"

def City(city, year):
    return ("You live in", city,"and are in grade", year)

def Recieving(z):
    return z

def twoNumbers(a,b):
    return random.randint(a,b)

def areaPlane(a,b):
    return "The box has an area of", (a*b), "units^2"

def Volume(a,b,c):
    return "The volume of the box is ",(a*b*c), "units^3"

print(areaPlane(float(input("What is the length? - ")), float(input("What is the width? - "))))

print(Volume(float(input("What is the length? - ")),float(input("What is the width? - ")),float(input("What is the height? - "))))

print(twoNumbers(float(input("What is your first number? - ")),float(input("What is your second number? - "))))

print(Recieving(input("What number?")))

print(myFunc(i,j))

print(mySchool())

print(calcGrade(int(input("What grade are you in? - "))))

print(City(input("What city do you live in? - "), int(input("What grade are you in? - "))))
