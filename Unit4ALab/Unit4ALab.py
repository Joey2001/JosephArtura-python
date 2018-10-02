def main():
    numbers = [23,46,46,78]
    multiply = 9;
    string = input("Now type - ")
    print(deVowel(string))
    print(mathStuff(numbers, multiply))

def deVowel(myString):
    newStr = myString
    vowels = ['a', 'e', 'i', 'o', 'u']
    for x in myString.lower():
        if x in vowels:
            newStr = newStr.replace(x,"")
    return newStr
def mathStuff(num, multiply):
    for i in range(len(num)):
        num[i] = num[i] * multiply
    return num

main()
