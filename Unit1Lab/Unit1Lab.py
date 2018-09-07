#print("I love Python")

#print("What is your name?")
#myName = input()
#print("\nMy name is",myName)

#if myName == "Joseph Artura":
#    print("Access Granted")
#else:
#    print("Access Denied\n")

base_64 = 2**64
numPi = 457
print(base_64, "\n", "\n", numPi)

num1_1 = input("What is the first number?\n")
num2_1 = input("What is the second number?\n")
num1 = float(num1_1)
num2 = float(num2_1)
#print("The answer to your question is",num1 + num2)

print("What would you like to do?\nAdd(+), Subtract(-), Multiply(*), Divide(/), Exponents(**), or Modulation(%)?")
assigned = input()
if assigned == "+":
    print("The answer is",num1 + num2)
if assigned == "-":
    print("The answer is",num1 - num2)
if assigned == "*":
    print("The answer is",num1 * num2)
if assigned == "/":
    print("The answer is",num1 / num2)
if assigned == "**":
    print("The answer is",num1 ** num2)
if assigned == "%":
    print("The answer is",num1 % num2)

