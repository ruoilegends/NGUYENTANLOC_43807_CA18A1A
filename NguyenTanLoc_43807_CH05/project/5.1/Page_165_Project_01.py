"""
Author: Nguyen Tan Loc
Date: 7/10/2021
Problem:A group of statisticians at a local college has asked you to create a set of functions
that compute the median and mode of a set of numbers, as defined in Section
5.4. Define these functions in a module named stats.py. Also include a function
named mean, which computes the average of a set of numbers. Each function
should expect a list of numbers as an argument and return a single number. Each
function should return 0 if the list is empty. Include a main function that tests the
three statistical functions with a given list.
Solution:


    ....
"""
def mean(lst):
    if not lst:
        return 0
    total = 0
    for num in lst:
        total += num
    return total / len(lst)
def median(lst):
    if not lst:
        return 0
    samples = sorted(lst.copy())
    if len(samples) % 2 == 1:
        return samples[int(len(samples) / 2)]
    else:
        return (samples[int(len(samples) / 2)] + samples[int(len(samples) / 2) - 1]) / 2
def mode(lst):
    if not lst:
        return 0
    result = lst[0]
    count = 0
    for num in lst:
        if lst.count(num) >= count:
            count = lst.count(num)
            result = num
    return result
def main():
    userList = [3, 1, 7, 1, 4, 10]
    print('List:', userList)
    print('Mode:', mode(userList))
    print('Median:', median(userList))
    print('Mean:', mean(userList))
main()