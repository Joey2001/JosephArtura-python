def main():
    month = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    weekends = {month[0] : [6, 7, 13, 14, 20, 21, 27, 28], month[1] : [3, 4, 10, 11, 17, 18, 24, 25], month[2] : [3, 4, 10, 11, 17, 18, 24, 25, 31], month[3] : [1,7,8,14,15,21,22,28,29], month[4] : [5,6,12,13,19,20,26,27], month[5] : [2,3,9,10,16,17,23,24,30], month[6] : [1,7,8,14,15,21,22,28,29], month[7] : [4,5,11,12,18,19,25,26], month[8] : [1,2,8,9,15,16,22,23,29,30], month[9] : [6,7,13,14,20,21,27,28], month[10] : [3,4,10,11,17,18,24,25], month[11] : [1,2,8,9,15,16,22,23,29,30]}
    monthInput = input("What is the month? - ").lower()
    dayInput = int(input("What is the day? - "))
    k = 0
    days = 0
    for i in range(len(month)):
        if(monthInput == month[i]):
            if(i < 9):
                monthInt1 = 0
                monthInt2 = i + 1
            else:
                monthInt1 = 1
                monthInt2 = i - 9
    for i in weekends:
        if(monthInput == i):
            for j in weekends[i]:
                if(dayInput == j):
                    print(str(monthInt1) + str(monthInt2) + '/' + str(dayInput) + '/18 falls on a weekend.')
                    days = j
    if(days == k):
        k += 1
        print(str(monthInt1) + str(monthInt2) + '/' + str(dayInput) + '/18 does not occur on a weekend.')
def repeat():
    play  = 'yes'
    while(play.lower() == 'yes'):
        main()
        play = input('\n' + "Do you want to check another date? \n")
repeat()
