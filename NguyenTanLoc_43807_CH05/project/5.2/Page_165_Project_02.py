"""
Author: Nguyen Tan Loc
Date: 7/10/2021
Problem:Write a program that allows the user to navigate the lines of text in a file. The
program should prompt the user for a filename and input the lines of text into a
list. The program then enters a loop in which it prints the number of lines in the
file and prompts the user for a line number. Actual line numbers range from 1 to
the number of lines in the file. If the input is 0, the program quits. Otherwise, the
program prints the line associated with that number
Solution:

    ....
"""
text = input('Enter file name: ')
with open(text, 'r') as file:
    data = []
    for line in file:
        data.append(line.strip())
print('The number of lines in the file is:', len(data))
while True:
   lnum = int(input('Enter line number: '))
   if lnum == 0:
       break
   else:
       num = lnum - 1
       print(data[num])
