"""
Author: Nguyen Tan Loc
Date: 10/09/2021
Problem:
   Write a loop that prints the first 128 ASCII values followed by the corresponding
characters (see the section on characters in Chapter 2). Be aware that most of the
ASCII values in the range “0..31” belong to special control characters with no standard print representation, so you might see strange symbols in the output for these
values.
Solution:
for count in range(1, 129, 1):
    a = chr(count)
    print(a)

    ....
"""