"""
Author: Nguyen Tan Loc
Date: 24/09/2021
Problem:
    You are given a string that was encoded by a Caesar cipher with an unknown distance value. The text can contain
    any of the printable ASCII characters. Suggest an algorithm for cracking this code.
Solution:
def caesarCipher(string, key):
encrypted string = ()
new_key = key % 26
for letter in string:
encrypted string.append(getNewLetter(letter, new_key))
return '.join(encrypted string)
def getNewletter(letter, key):
new_letter = ord(letter) + key return chr(new_letter) if new letter <= 122 else chr(96 + new_letter122)
print (caesarCipher('hell0'))
    ....
"""