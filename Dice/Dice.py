import random
DICENUM = 2
def main():
    count = 0
    setOfDice = constructDice()
    while((input("Do you want to play again? (\'y\' or \'n\') - ") == 'y')):
        diceSet = [0] * DICENUM
        for i in range(DICENUM):
            roll = randInt()
            diceSet[i] = setOfDice[roll]
        dicePrint(diceSet)
        count += 1
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
def dicePrint(allDice):
    for dice in range(len(allDice[0])):
        for side in range(len(allDice)):
            print(allDice[side][dice], end = '\t')
        print()


def randInt():
    return random.randint(0,5)
main()
