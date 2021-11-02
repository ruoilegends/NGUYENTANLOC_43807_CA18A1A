"""
Author: Nguyen Tan Loc
Date: 7/10/2021
Problem:
Write a program that inputs a text file. The program should print the unique
words in the file in alphabetical order.

Solution:

    ....
"""
unique = []

with open("bai.txt", "r") as file:
   lines = file.readlines()
   for line in lines:
       words = line.split()
       for word in words:
           word = word.strip()
           if word not in unique:
               unique.append(word)
unique = sorted(unique)
print(unique)