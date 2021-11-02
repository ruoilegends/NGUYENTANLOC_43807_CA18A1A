"""
Author: Nguyen Tan Loc
Date: 22/10/2021
Problem:
Write the code for a mapping that generates a list of the absolute values of the numbers in a list named numbers
Solution:
 Map Function
        • Map is one of the higher order functions in python used to apply a specific function on all the elements
    of an iterable object.
        • Iterable objects are those that contains group of elements entitled under a single name like lists,
    dictionaries, tuples and so on.
        • The function that is applied using map can be a built-in function or any user defined function.
        • Map function returns a map object which should be casted according to our requirement.
        • The general syntax of map function will be as follows
        map (function, iterable object)
        • According to the requirement of the problem a mapping that generates a list of absolute values of the
    numbers in a list named “numbers” should be written.
        • The code for mapping will be as follows
        print (list (map (abs, numbers)))
        • “abs” is the name of the function that takes a single value as an argument and return the absolute value
    of that respective argument.
        • “numbers” is the list data structure that contains a list of numbers
        • “map” is the function that maps each element of the list “numbers” to the function “abs”.
"""
#example
myList = [2,3,-3,-2]
print (map(abs, myList))

