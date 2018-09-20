num = [4,9,15,60]
def Double():
   global num_Two
   num_Two = [i * 2 for i in num]
   print(num)
   print(num_Two)

def TripleDouble():
    num_Three = [i * 3 for i in num_Two]
    print(num_Three)

Double()
TripleDouble()
