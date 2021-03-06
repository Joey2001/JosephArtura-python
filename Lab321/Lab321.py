def main():
    #list of predefined grades
    #grades = [86.8,67.6,98.9,92.1]
    num = int(input("How many grades? - "))
    grades = getGrade(num)
    #shortcut for the function Grade
    average = Grade(grades)
    #input for what school
    school = input("What school do you go to? - ")
    #prints the input for what school
    print(school, "Student")
    #asks for year
    year = int(input("What grade are you in? - "))
    #prints if you are a Freshman, Sophomore, Junior,Senior or not in high school
    print("You are", Year(year))
    #Makes sure that you are given an average grade if you are in high school
    if 8 < year < 13:
        #averages the numbers in the list
        print("Your average grade is", average)
        #gives you a letter grade based on the average
        print("Your letter grade is", Letter(average))

def getGrade(num):
    #intialize the list
    grades = []
    #appends the list for a certain range
    for i in range(num):
        #input number to add to the list
        myNum = float(input("What is the grade? - "))
        #adds the number to the list
        grades.append(myNum)
    #returns the grades as a list
    return grades

def Grade(grades):
    #initialize the variable average
    average = 0
    #sets average to previous sum, so makes summation
    for i in range(len(grades)):
        average = average + float(grades[i])
    #returns the average by taking the number from the for loop and dividing by the length of the list
    return average/len(grades)

def Year(year):
    #tests if you are in high school or not, and specifies if you are a Freshman, Sophomore, Junior, or Senior
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
    #returns to main
    return strYear

def Letter(average):
    #tests what letter grade should be given
    if average > 90:
        letterGrade = "A"
    elif average > 80:
        letterGrade = "B"
    elif average > 70:
        letterGrade = "C"
    elif average > 60:
        letterGrade = "D"
    elif 0 <= average < 59:
        letterGrade = "F"
    else:
        letterGrade = "Please enter valid numbers"
    #returns to main
    return letterGrade
main()
