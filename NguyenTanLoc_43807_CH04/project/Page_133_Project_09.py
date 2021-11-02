"""
Author: Nguyen Tan Loc
Date: 24/09/2021
Problem:
write a script named numberlines.py. This script creates a program listing from a
source program. This script should prompt the user for the names of two files. The
input filename could be the name of the script itself, but be careful to use a different
output filename! The script copies the lines of text from the input file to the output
file, numbering each line as it goes. The line numbers should be right-justified in
4 columns, so that the format of a line in the output file looks like this example:
1> This is the first line of text.
Solution:

    ....
"""
inputFileName = input("Input filename: ")
outputFileName = input("Output filename: ")
inputFile = open(inputFileName, "r")
outputFile = open(outputFileName, "w")
count = 1
for line in inputFile:
    newLine = str(count).rjust(4, " ") + "> " + line
    outputFile.write(newLine)
    count += 1
print(newLine)



