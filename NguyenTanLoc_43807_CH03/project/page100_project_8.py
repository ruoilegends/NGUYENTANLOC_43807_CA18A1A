"""
Author: Nguyen Tan Loc
Date: 10/09/2021
Problem: The greatest common divisor of two positive integers, A and B, is the largest
number that can be evenly divided into both of them. Euclid’s algorithm can be
used to find the greatest common divisor (GCD) of two positive integers. You
can use this algorithm in the following manner:
a. Compute the remainder of dividing the larger number by the smaller
number.
b. Replace the larger number with the smaller number and the smaller number
with the remainder.
c. Repeat this process until the smaller number is zero.
The larger number at this point is the GCD of A and B. Write a program that lets
the user enter two integers and then prints each step in the process of using the
Euclidean algorithm to find their GCD.
Solution:

"""


# Defining the function to calculate the GCD
def EuclideanGCD(A, B):
    if A < B:
        A, B = B, A

    # Base Condtion
    if (A % B) == 0:
        return B

        # Recursive Call
    else:
        T = A % B
        return (EuclideanGCD(B, T))

    # Input the numbers


A = int(input('Enter the first number : '))
B = int(input('Enter the second number : '))

# Print the GCD
print('GCD : ', EuclideanGCD(A, B))

