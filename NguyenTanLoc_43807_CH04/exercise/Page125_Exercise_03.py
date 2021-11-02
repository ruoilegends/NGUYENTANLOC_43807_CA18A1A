"""
Author: Nguyen Tan Loc
Date: 24/09/2021
Problem:
   Assume that a file contains integers separated by newlines. Write a code segment
that opens the file and prints the average value of the integers.
Solution:
f = open("integers.txt", 'r')
theSum = 0
for line in f:
 line = line.strip()
 number = int(line)
 theSum += number
print("The sum is", theSum)
    ....
"""