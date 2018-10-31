import random
DICENUM = 2
def main():
    count = 0
    countDice = []
    play = 'y'
    setOfDice = constructDice()
    while(count < 100):
        diceSet = [0] * DICENUM
        addSets = []
        for i in range(DICENUM):
            roll = randInt()
            addSets.append(roll + 1)
            diceSet[i] = setOfDice[roll]
        countDice.append(sum(addSets))
        print(addSets)
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
    print("You have rolled a one", count1, "times")
    print("You have rolled a two", count2, "times")
    print("You have rolled a three", count3, "times")
    print("You have rolled a four", count4, "times")
    print("You have rolled a five", count5, "times")
    print("You have rolled a six", count6, "times")

def dicePrint(allDice):
    for dice in range(len(allDice[0])):
        for side in range(len(allDice)):
            print(allDice[side][dice], end = '\t')
        print()

def randInt():
    return random.randint(0,5)
main()
