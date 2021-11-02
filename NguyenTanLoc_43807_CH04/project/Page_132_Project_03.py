"""
Author: Nguyen Tan Loc
Date: 24/09/2021
Problem:
Write a script that inputs a line of encrypted text and a distance value and outputs
plaintext using a Caesar cipher. The script should work for any printable characters.
Solution:

    ....
"""
cipher=input("enter the coded text: ")
shift=int(input("enter the distance value: "))
plaintext=''
for c in cipher:
    new_dist=ord(c)-(shift%128)
    if new_dist<0:
        new_dist=128+new_dist
    plaintext=plaintext+chr(new_dist)
print(plaintext)