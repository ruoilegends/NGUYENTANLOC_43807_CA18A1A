"""
Author: Nguyen Tan Loc
Date: 24/09/2021
Problem:
    Assume that the variable data refers to the string "Python rules!". Use a string
method from Table 4-2 to perform the following tasks:
a. Obtain a list of the words in the string.
b. Convert the string to uppercase.
c. Locate the position of the string "rules".
d. Replace the exclamation point with a question mark.
Solution:
a.
data="Python rNes!"
print(data.split()
OUTPUT: ['Python, 'rules!']
b.
data="Python rules!"
print(data.uppper ()
OUTPUT: PYTHON RULES!
c.
data="Python rules!"
print(data.find ("rules")
OUTPUT:
7
d.
data="Python rules!"
print(data.replace("!""?"))
OUTPUT: Python rules?
    ....
"""