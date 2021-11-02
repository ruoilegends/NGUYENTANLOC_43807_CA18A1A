"""
Author: Nguyen Tan Loc
Date: 24/09/2021
Problem:
Octal numbers have a base of eight and the digits 0–7. Write the scripts octalToDecimal.py and decimalToOctal.py, which convert numbers between the octal
and decimal representations of integers. These scripts use algorithms that are
similar to those of the binaryToDecimal and decimalToBinary scripts developed in Section 4-3.
Solution:

       Binary to Decimal code:

"""
bstring = input("Enter a string of bits: ")
decimal = 0
exponent = len(bstring) - 1
for digit in bstring:
    decimal = decimal + int(digit) * 2 ** exponent
    exponent = exponent - 1
print("The integer value is", decimal)

