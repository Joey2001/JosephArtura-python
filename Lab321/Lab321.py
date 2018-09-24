grades = [86.8,67.6,98.9,92.1]
def main():
    print(school(), "Student")
    print("You are", Year())
    print("Your average grade is", Grade())
    print("Your letter grade is", Letter())

def Grade():
    average = float(((grades[0]+grades[1]+grades[2]+grades[3])/len(grades)))
    return average

def Year():
    year = int(input("What grade are you in? - "))
    if year == 9:
        strYear = "a Freshman"
    elif year == 10:
        strYear = "a Sophomore"
    elif year == 11:
        strYear = "a Junior"
    elif year == 12:
        strYear = "a Senior"
    else:
        strYear = "not in high school"
    return strYear

def Letter():
    if Grade() > 90:
        letterGrade = "A"
    elif Grade() > 80:
        letterGrade = "B"
    elif Grade() > 70:
        letterGrade = "C"
    elif Grade() > 60:
        letterGrade = "D"
    elif 0 <= Grade() < 59:
        letterGrade = "F"
    else:
        letterGrade = "Please enter valid numbers"
    return letterGrade
def school():
    return input("What school do you go to? - ")
main()
