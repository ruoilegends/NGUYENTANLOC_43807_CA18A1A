"""
Author: Nguyen Tan Loc
Date: 24/09/2021
Problem:
A bit shift is a procedure whereby the bits in a bit string are moved to the left or
to the right. For example, we can shift the bits in the string 1011 two places to
the left to produce the string 1110. Note that the leftmost two bits are wrapped around to the right side
of the string in this operation. Define two scripts, shiftLeft.py and shiftRight.py, that expect a bit
string as an input. The script shiftLeft shifts the bits in its input one place to the left, wrapping the leftmost bit
to the rightmost position. The script shiftRight performs the inverse operation.
Each script prints the resulting string.
Solution:

    ....
"""
def shiftleft(bitstring):
    bitstring=bitstring[1:]+bitstring[0]
    return bitstring
bit=input("enter a string of bits : ")
leftshift= shiftleft(bit)
print(leftshift)


