import random
DICENUM = 3
def main():
    count = 0
    countDice = []
    play = 'y'
    setOfDice = constructDice()
    while(count < 10000):
        diceSet = [0] * DICENUM
        addSets = []
        for i in range(DICENUM):
            roll = randInt()
            addSets.append(roll + 1)
            diceSet[i] = setOfDice[roll]
        countDice.append(sum(addSets))
        dicePrint(diceSet)
        print(addSets)
        print(countDice)
        numberCount(countDice)
        count += 1
        #play = input("Do you want to play again? (\'y\' or \'n\') - ")
    if(count > 1):
        print("You have played", count, "times.")
    elif(count == 1):
        print("You have played one time.")
    else:
        print("You have not played.")

def constructDice():
    topBottom = ' ------- '
    leftOne =   '| *     |'
    middleOne = '|   *   |'
    rightOne =  '|     * |'
    middleTwo = '| *   * |'
    empty =     '|       |'
    One = [topBottom, empty, middleOne, empty, topBottom]
    Two = [topBottom, empty, middleTwo, empty, topBottom]
    Three = [topBottom, leftOne, middleOne, rightOne, topBottom]
    Four = [topBottom, middleTwo, empty, middleTwo, topBottom]
    Five = [topBottom, middleTwo, middleOne, middleTwo, topBottom]
    Six = [topBottom, middleTwo, middleTwo, middleTwo, topBottom]
    allDice = [One, Two, Three, Four, Five, Six]
    return allDice

def numberCount(countDice):
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    count6 = 0
    count7 = 0
    count8 = 0
    count9 = 0
    count10 = 0
    count11 = 0
    count12 = 0
    count13 = 0
    count14 = 0
    count15 = 0
    count16 = 0
    count17 = 0
    count18 = 0
    for i in range(len(countDice)):
        if countDice[i] == 1:
            count1 += 1
        if countDice[i] == 2:
            count2 += 1
        if countDice[i] == 3:
            count3 += 1
        if countDice[i] == 4:
            count4 += 1
        if countDice[i] == 5:
            count5 += 1
        if countDice[i] == 6:
            count6 += 1
        if countDice[i] == 7:
            count7 += 1
        if countDice[i] == 8:
            count8 += 1
        if countDice[i] == 9:
            count9 += 1
        if countDice[i] == 10:
            count10 += 1
        if countDice[i] == 11:
            count11 += 1
        if countDice[i] == 12:
            count12 += 1
        if countDice[i] == 13:
            count13 += 1
        if countDice[i] == 14:
            count14 += 1
        if countDice[i] == 15:
            count15 += 1
        if countDice[i] == 16:
            count16 += 1
        if countDice[i] == 17:
            count17 += 1
        if countDice[i] == 18:
            count18 += 1
    if DICENUM >= 1:
        if DICENUM == 1:
            print("You have rolled a one", count1, "times")
        if DICENUM == 1 or DICENUM == 2:
            print("You have rolled a two", count2, "times")
        print("You have rolled a three", count3, "times")
        print("You have rolled a four", count4, "times")
        print("You have rolled a five", count5, "times")
        print("You have rolled an six", count6, "times")
    if DICENUM > 1:
        print("You have rolled a seven", count7, "times")
        print("You have rolled an eight", count8, "times")
        print("You have rolled a nine", count9, "times")
        print("You have rolled a ten", count10, "times")
        print("You have rolled an eleven", count11, "times")
        print("You have rolled a twelve", count12, "times")
    if DICENUM > 2:
        print("You have rolled a thirteen", count13, "times")
        print("You have rolled an fourteen", count14, "times")
        print("You have rolled a fifteen", count15, "times")
        print("You have rolled a sixteen", count16, "times")
        print("You have rolled an seventeen", count17, "times")
        print("You have rolled an eighteen", count18, "times")

def dicePrint(allDice):
    for dice in range(len(allDice[0])):
        for side in range(len(allDice)):
            print(allDice[side][dice], end = '\t')
        print()

def randInt():
    return random.randint(0,5)
main()
