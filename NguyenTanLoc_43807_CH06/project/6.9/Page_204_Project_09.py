"""
Author: Nguyen Tan Loc
Date: 7/10/2021
Problem:
Write a program that computes and prints the average of the numbers in a text
file. You should make use of two higher-order functions to simplify the design.
Solution:


    ....
"""
from functools import reduce
filename = input("enter input the filename :")
inputfile= open(filename,'r')
lyst=[]
for line in inputfile :
    lyst.extend(line.split())
lyst=list(map(float,lyst))
sum = reduce(lambda x,y:x+y,lyst)
if len(lyst)==0:
    average=0
else:
    average = sum/len(lyst)
print("the average is :", average)