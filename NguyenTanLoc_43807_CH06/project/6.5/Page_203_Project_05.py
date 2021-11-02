"""
Author: Le Van The
Date: 23/10/2021
Problem:
A list is sorted in ascending order if it is empty or each item except the last one is
less than or equal to its successor. Define a predicate isSorted that expects a list
as an argument and returns True if the list is sorted, or returns False otherwise.(Hint: For a list of length 2 or greater, loop through the list and compare pairs of
items, from left to right, and return False if the first item in a pair is greater.)
Solution:


    ....
"""
def isSorted(lyst):
    """Returns True if lyst is sorted in ascending order or False otherwise."""
    if len(lyst) == 0 or len (lyst) == 1:
        return True
    else:
        for index in range(len(lyst) - 1):
            if lyst[index] > lyst[index + 1]:
                return False
    return True


def main():
    Lyst = []
    print(isSorted(Lyst))
    Lyst = [1]
    print(isSorted (Lyst))
    Lyst = list(range (10))
    print(isSorted (Lyst))
    Lyst[9] = 3
    print(isSorted (Lyst))


main()