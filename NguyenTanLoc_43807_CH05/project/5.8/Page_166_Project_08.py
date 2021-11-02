"""
Author: Nguyen Tan Loc
Date: 7/10/2021
Problem:
A file concordance tracks the unique words in a file and their frequencies. Write
a program that displays a concordance for a file. The program should output the
unique words and their frequencies in alphabetical order. Variations are to track
sequences of two words and their frequencies, or n words and their frequencies
Solution:

    ....
"""
filename=input('Enter the input file name: ')
inputFile = open(filename,"r+")
list={}
for word in inputFile.read().split():
  if word not in list:
     list[word] = 1
  else:
     list[word] += 1
inputFile.close();
print();
for i in sorted(list):
  print("{0} {1} ".format(i, list[i]));