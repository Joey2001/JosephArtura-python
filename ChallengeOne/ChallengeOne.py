num = [4,9,15,60]
def Double():
   global num_Two
   num_Two = [i * 2 for i in num]
   print(num)
   print(num_Two)

def TripleDouble():
    global num_Three
    num_Three = [i * 3 for i in num_Two]
    print(num_Three)

def Exponential():
    num_Four = [i**2 for i in num_Three]
    print(num_Four)

Double()
TripleDouble()
Exponential()
