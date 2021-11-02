"""
Author: Nguyen Tan Loc
Date: 24/09/2021
Problem:
Write a script named copyfile.py. This script should prompt the user for the
names of two text files. The contents of the first file should be input and written
to the second file.
Solution:

    ....
"""
file1= input('\nPlease enter name of first file: ')
file2 = input('Please enter name of Second file: ')
with open(file1) as f:
    with open(file2, "w") as f1:
        for line in f:
            f1.write(line)
log = open(file2, "r")
for line in log:
    print(line)



