"""
Author: Nguyen Tan Loc
Date: 7/10/2021
Problem:
 Explain the difference between structural equivalence and object identity.
Solution:
The Object Identity refers to when we create alias to one variable and wanted check whether they both refers
to the same object or not. That means the two different variables referring to same obiect.
The "is" operator can be used to check the object identity. It returns "“True" if the two variables refer to same object
 and it returns "False" if the variables refer to different objects.
Consider the following example which explains about object identity.
a=10
b=a
Now both the variables "a" and "b" refer to the same object or the value 10.
    ....
"""