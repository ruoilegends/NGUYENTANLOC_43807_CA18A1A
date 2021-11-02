"""
Author: Nguyen Tan Loc
Date: 10/09/2021
Problem:
Write a program that receives a series of numbers from the user and allows the
user to press the enter key to indicate that he or she is finished providing inputs.
After the user presses the enter key, the program should print the sum of the
numbers and their average.
Solution:

"""
theSum = 0
count = 0
average = 0


while True:
    num = input("Enter a number: ")
    if num =="":
        break
    theSum += float(num)
    count  += 1
average = float(theSum/count)
print("The sum is", theSum)
print("the average is : ", average)



