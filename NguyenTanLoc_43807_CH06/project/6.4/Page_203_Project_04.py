"""
Author: Le Van The
Date: 23/10/2021
Problem:
Restructure Newton’s method (Case Study 3.6) by decomposing it into three
cooperating functions. The newton function can use either the recursive strategy
of Project 1 or the iterative strategy of Case Study 3.6. The task of testing for the
limit is assigned to a function named limitReached, whereas the task of computing a new approximation is assigned to a function named improveEstimate. Each
function expects the relevant arguments and returns an appropriate value.
Solution:


    ....
"""
import math


# Initialize the tolerance
TOLERANCE = 0.000001


def newton (x, estimate=1):
    """Returns the square röot of x."""
    # Compute the difference and test for the base case
    if limitReached (x, estimate):
        return estimate
    else:
    # Recurse after improving the estimate
        return newton (x, improveEstimate (x, estimate))
def limitReached(x, estimate):
    """Returns True if the estimate is within the tolerance or False otherwise."""
    difference = abs (x - estimate ** 2)
    return difference <= TOLERANCE
def improveEstimate(x, estimate):
    """Returns an improved estimate."""
    return (estimate + x / estimate) / 2
def main():
    """Allows the user to obtain square roots."""
while True:
    # Receive the input number from the user
    x = input("Enter a positive number or enter/return to quit: ")
    if x == "":
        break
    x = float(x)
    # Output the result
    print("The program's estimate is", newton (x))
    print("Python's estimate is ", math.sqrt(x))


main()