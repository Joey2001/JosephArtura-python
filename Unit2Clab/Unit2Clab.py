numList = [12,24,36,48,60,72,84,96,108,120]
print(numList)
print(len(numList))

subList = numList[0:5]
print(subList)
number = subList.append(69)
print(subList)

subList1 = numList+[(45**8)]
print(subList1)

myClasses = ["AP Computer Science A","AP Calculus BC","Senior Lit: Shakespeare", "Senior Composition", "Python", "AP Physics C", "AP Government"]
favClass = myClasses[5]
leastFavClass = myClasses.pop(6)
print(myClasses)
print("My favorite class is",favClass)
