numGrade = float(input("What is your grade?\n"))
x=0
if numGrade >= 90:
    print("Yahoo you got an A!")
elif numGrade >= 80:
    print("Good you got a B!")
elif numGrade >= 70:
    print("Okay you got a C!")
else:
    print("You better study harder")
color = ['red','orange','yellow','green','blue','purple','violet','pink','black','white','indigo']
userInput = input("\nWhat is your favorite color?\n").lower()

for x in range(0,10):
    if userInput == color[x]:
        print(color[x], "is my favorite color too!")

if userInput == color[4]:
    print("The sky is blue")
elif userInput == color[3]:
    print("The Forest is green")
elif userInput == color[0]:
    print("I love red")
elif userInput == color[2]:
    print("Yuck Yellow")
else:
    print("I'm a dumb computer - I only know 4 colors")
