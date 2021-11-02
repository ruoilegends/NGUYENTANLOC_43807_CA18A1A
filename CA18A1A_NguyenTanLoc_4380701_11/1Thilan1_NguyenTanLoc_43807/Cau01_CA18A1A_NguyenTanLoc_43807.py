"""
De thi 02
Date: 01/11/2021
Nguyen Tan Loc
"""
# câu 1:

bstring = input("Enter a string of bits: ")
decimal = 0
exponent = len(bstring) - 1
for digit in bstring:
        decimal = decimal + int(digit) * 2 ** exponent
        exponent = exponent - 1
print("The integer value is", decimal)






