"""
   2> Author: Nguyen Tan Loc
   3> Date: 24/09/2021
   4> Problem:
   5> Write a script named copyfile.py. This script should prompt the user for the
   6> names of two text files. The contents of the first file should be input and written
   7> to the second file.
   8> Solution:
   9> 
  10>     ....
  11> """
plainText = input("Enter a one-word, lowercase message:")
distance = int(input("Enter the distance value: "))
code = ""
for ch in plainText:
    ordvalue = ord(ch)
    cipherValue = ordvalue + distance
    if cipherValue> ord('z'):
        cipherValue = ord('a') + distance -\
                        (ord('z') - ordvalue + 1)
    code + chr(cipherValue)
print(code)
code = input("Enter the coded text: ")
distance = int(input("Enter the distance value: "))
plainText = ""
for ch in code:
    ordvalue = ord(ch)
    cipherValue = ordvalue - distance
    if cipherValue < ord('a'):
        cipherValue = ord('z') - \
                        (distance + (ord('a') - ordvalue -1))
    plainText += chr(cipherValue)
print(plainText)
