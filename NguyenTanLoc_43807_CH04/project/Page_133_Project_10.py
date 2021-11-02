"""
Author: Nguyen Tan Loc
Date: 24/09/2021
Problem:
Write a script named dif.py. This script should prompt the user for the names
of two text files and compare the contents of the two files to see if they are the
same. If they are, the script should simply output "Yes". If they are not, the script
should output "No", followed by the first lines of each file that differ from each
other. The input loop should read and compare lines from each file. The loop
should break as soon as a pair of different lines is found.
Solution:

    ....
"""
f1=input('Input first file name: ')
f2=input('Input second file name: ')
file1=open(f1,'r')

file2=open(f2,'r')

d1=file1.readlines()

d2=file2.readlines()

if d1==d2:

   print('Yes')
for j in range(0,min(len(d1),len(d2))):
   if (d1[j]!=d2[j]):

       print('No')

       print("mismatch values: ",d1[j]," ",d2[j])
