"""
Author: Nguyen Tan Loc
Date:24/09/2021
Problem:
Use the strategy of the decimal to binary conversion and the bit shift left operation defined in Project 5 to code a new encryption algorithm. The algorithm
should add 1 to each character’s numeric ASCII value, convert it to a bit string,
and shift the bits of this string one place to the left. A single-space character in
the encrypted string separates the resulting bit strings.
Solution:

    ....
"""
decimal = int(input("Enter a decimal integer: "))
if decimal == 0:
    print(0)
else:
    print("Quotient Remainder Binary")
    bitString = ""
    while decimal > 0:
        remainder = decimal % 2
        decimal = decimal // 2
        bitString = str(remainder) + bitString
        print("%5d%8d%12s" % (decimal, remainder,bitString))
print("The binary representation is", bitString)

