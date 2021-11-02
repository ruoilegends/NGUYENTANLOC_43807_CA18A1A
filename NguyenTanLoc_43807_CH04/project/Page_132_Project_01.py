"""
Author: Nguyen Tan Loc
Date: 24/09/2021
Problem:
Write a script that inputs a line of plaintext and a distance value and outputs an
encrypted text using a Caesar cipher. The script should work for any printable
characters.
Solution:

    ....
"""
#consider printable characters with ascii values from 32 to 126.
maxValue = 126
minValue = 32
count = maxValue - minValue + 1
plainText = input ("Enter plaintext: ") #input plaintext
distance = int (input ("Enter distance: ")) #input distance
encryptedText =''
# iterate over all the characters of given plainText
for i in plainText: asciivalue = ord (i) #find ascii value of the character
# #add distance to ascii value to get caesar cipher value
caesarvalue = asciivalue + distance
# if caesar value is greater than 126 or less than 32
caesarValue = caesarvalue * count
#if value is less than minValue, add count
if caesarValue < minValue:
 caesarvalue += count
 # caesarValue += minValue
 encryptedText += chr (caesarValue)
 print(encryptedText)
