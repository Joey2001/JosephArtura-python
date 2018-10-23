import random
def main():
    count = 0
    dicePrint(randInt())
    count += 1
    while((input("Do you want to play again? (\'y\' or \'n\') - ") == 'y')):
        main()
    if(count > 1):
        print("You have played", count,"times.")
    else:
        print("You have played one time.")

def dicePrint(diceNum):
    topBottom = ' ------- \n'
    leftOne =   '| *     |\n'
    middleOne = '|   *   |\n'
    rightOne =  '|     * |\n'
    middleTwo = '| *   * |\n'
    empty =     '|       |\n'
    One = topBottom + empty + middleOne + empty + topBottom
    Two = topBottom + empty + middleTwo + empty + topBottom
    Three = topBottom + leftOne + middleOne + rightOne + topBottom
    Four = topBottom + middleTwo + empty + middleTwo + topBottom
    Five = topBottom + middleTwo + middleOne + middleTwo + topBottom
    Six = topBottom + middleTwo + middleTwo + middleTwo + topBottom
    print(One + Two + Three + Four + Five + Six)
    if diceNum == 1:
        print(One)
    elif diceNum == 2:
        print(Two)
    elif diceNum == 3:
        print(Three)
    elif diceNum == 4:
        print(Four)
    elif diceNum == 5:
        print(Five)
    elif diceNum == 6:
        print(Six)
    else:
        return "No dice"

def randInt():
    return random.randint(1,6)
main()
