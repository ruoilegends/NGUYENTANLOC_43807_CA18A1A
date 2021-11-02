"""
Author: Nguyen Tan Loc
Date: 22/10/2021
Problem:
 In what way is a recursive design different from top-down design?
Solution:
Recursive functions
 • Recursive functions are a type of functions in which the same function it called itself in the body of the function.
 • A recursion should have a base case and an iteration case.
 • The base case is the termination point at which the program should halt. If the base case is not perfect then the program never terminates and fall into infinite recursion.
 • In case of infinite recursion, the python virtual machine runs out of memory and halts its execution indicating a "stack overflow error"
 • The iteration case tells about how the function should be iterated to get the expected output.
 • Recursion reduces the size of the code and makes the code look more elegant.

 Differences between Top-down and Recursive designs
 *Top-Down design Recursive Design
  -In Top-down approach we divide a complex problem into two or more sub-problems that are isolated and are provided with a
  specific task to perform. This is known as problem decomposition In Recursive design a problem is divided into two or more
   sub problems of same type in such a way that all the sub problems can be solved using same recursive definition.
  -The sub problems involved in top-down design are not of same type.
  - The decomposed sub problems are not related to each The decomposed sub problems are related to each other other.
  -The sub problems are isolated and provided different unique tasks to be performed by each function.
  All the sub problems are solved using the same recursive definition.
    ....
"""