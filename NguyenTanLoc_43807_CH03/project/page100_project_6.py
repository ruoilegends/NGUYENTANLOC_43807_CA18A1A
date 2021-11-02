"""
Author: Nguyen Tan Loc
Date: 10/09/2021
Problem: The German mathematician Gottfried Leibniz developed the following method
to approximate the value of π:
π/4 5 1 ] 1/3 1 1/5 ] 1/7 1 . . .
Write a program that allows the user to specify the number of iterations used in
this approximation and that displays the resulting value.
Solution:

"""
def main():
    result=0
    n=int(input('Enter the number of iterations:'))
    for n in range(n):
        result += (-1.0) ** n / (2.0 * n + 1.0)

    print('The approximation of pi is ',4*result)
main()
