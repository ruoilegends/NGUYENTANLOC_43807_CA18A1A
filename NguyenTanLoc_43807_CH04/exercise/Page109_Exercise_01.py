"""
Author: Nguyen Tan Loc
Date: 24/09/2021
Problem:
    Write the encrypted text of each of the following words using a Caesar cipher with
a distance value of 3:
a. python
b. hacker
c. wow
Solution:
code = input("Enter the coded text: ")
distance = int(input("Enter the distance value: "))
plainText = ""
for ch in code:
 ordvalue = ord(ch)
 cipherValue = ordvalue - distance
 if cipherValue < ord('a'):
 cipherValue = ord('z') - \
 (distance - (ord('a') - ordvalue - 1))
 plainText += chr(cipherValue)
print(plainText
    ....
"""