def main():
    star(7)
    print()
    stripStar(3,7)
    print()
    pyramid(7)
    print()
    box(4,7)
def star(nums):
    for i in range(nums):
        starStr = ''
        for i in range(nums):
            starStr += '* '
        print(starStr)
def stripStar(height, width):
    for i in range(height):
        starStr = ''
        stripStr = ''
        for j in range(width):
            starStr += '* '
            stripStr += '- '
        print(starStr)
        print(stripStr)
def pyramid(num):
    for i in range(num):
        for j in range(i):
            print(str(i), end = '')
        print()
    for k in range(num,0,-1):
        for j in range(k):
            print(str(k), end = '')
        print()
def box(height, width):
    for j in range(width):
        print('*', end = '')
    print()
    for l in range(height):
        print('*', end = '')
        for k in range(width-2):
            print('-', end = '')
        print('*')
    for j in range(width):
        print('*', end = '')
main()
