import random
DICENUM = 10
def main():
    count = 0
    countDice = []
    play = 'y'
    setOfDice = constructDice()
    while(count < 10000000):
        diceSet = [0] * DICENUM
        addSets = []
        for i in range(DICENUM):
            roll = randInt()
            addSets.append(roll + 1)
            diceSet[i] = setOfDice[roll]
        countDice.append(sum(addSets))
        count += 1
    dicePrint(diceSet)
    print(addSets)
    print(countDice)
    numberCount(countDice)
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
    count = [0] * (DICENUM * 6)
    for i in range(len(countDice)):
        count[countDice[i] -1] += 1

    for i in range((DICENUM - 1), DICENUM * 6):
        print("You have rolled a", (i + 1), "-", count[i], "times.")

def dicePrint(allDice):
    for dice in range(len(allDice[0])):
        for side in range(len(allDice)):
            print(allDice[side][dice], end = '\t')
        print()

def randInt():
    return random.randint(0,5)
main()
