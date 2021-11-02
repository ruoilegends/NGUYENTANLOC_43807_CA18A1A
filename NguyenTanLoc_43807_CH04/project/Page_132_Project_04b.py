"""
Author: Nguyen Tan Loc
Date: 24/09/2021
Problem:
Octal numbers have a base of eight and the digits 0–7. Write the scripts octalToDecimal.py and decimalToOctal.py, which convert numbers between the octal
and decimal representations of integers. These scripts use algorithms that are
similar to those of the binaryToDecimal and decimalToBinary scripts developed in Section 4-3.
Solution:

    Decimal to Binary code:

"""
decimal = int(input("Enter a decimal integer: "))
if decimal == 0:
    print(0)
else:
    print("Quotient Remainder Binary")
    bstring = ""
    while decimal > 0:
        remainder = decimal % 2
        decimal = decimal // 2
        bstring = str(remainder) + bstring
        print("%5d%8d%12s" % (decimal, remainder, bstring))
    print("The binary representation is", bstring)

