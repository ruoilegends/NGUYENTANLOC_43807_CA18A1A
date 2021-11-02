"""
Author: Nguyen Tan Loc
Date: 22/10/2021
Problem:
Explain what happens when the following recursive function is called with the value
4 as an argument:
def example(n):
   if n > 0:
        print(n)
        example(n - 1)
Solution:
Recursive functions
 • Recursive functions are a type of functions in which the same function it called itself in the body of the function.
 • A recursion should have a base case and an iteration case.
 • The base case is the termination point at which the program should halt. If the base case is not perfect then the program never terminates and fall into infinite recursion.
 • In case of infinite recursion, the python virtual machine runs out of memory and halts its execution indicating a "stack overflow error"
 • The iteration case tells about how the function should be iterated to get the expected output.
 • Recursion reduces the size of the code and makes the code look more elegant.
    ....
"""