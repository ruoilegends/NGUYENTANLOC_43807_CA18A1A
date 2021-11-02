"""
Author: Le Van The
Date: 23/10/2021
Problem:
Elena complains that the recursive newton function in Project 2 includes an extra
argument for the estimate. The function’s users should not have to provide this
value, which is always the same, when they call this function. Modify the definition of the function so that it uses a keyword argument with the appropriate
default value, and call the function without a second argument to demonstrate
that it solves this problem.
Solution:


    ....
"""
import math

# Initialize the tolerance
TOLERANCE = 0.000001

def newton (x, estimate=1):
    """Returns the square root of x."""
    # Compute the difference and test for the base case
    difference = abs (x - estimate ** 2)
    if difference <= TOLERANCE:
        return estimate
    else:
        # Recurse after improving the estimate
        return newton (x, (estimate + x / estimate) / 2)
def main():
    """Allows the user to obtain square roots."""
    while True:
       # Receive the input number from the user
       x = input("Enter a positive number or enter/return to quit: ")
       if x == "":
           break
       x = float(x)
       # Output the result
       print("The program's estimate is", newton(x))
       print("Python's estimate is ", math.sqrt(x))
main()