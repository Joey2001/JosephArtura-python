
def changeNumbers(list, multiplier, expon):
    for i in range(len(list)):
        list[i] = (list[i]**expon) * multiplier
    return list

e = 3
results = changeNumbers([2,3,4,5], 2, e)
print(results)
print()
results = changeNumbers(results, 3, e)
print(results)
print()
results = changeNumbers(results, 10, e)
print(results)
