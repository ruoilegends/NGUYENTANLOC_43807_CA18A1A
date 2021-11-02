"""
Author: Nguyen Tan Loc
Date: 24/09/2021
Problem:
   Write a code segment that prints the names of all of the items in the current
working directory.
Solution:

import os
currentDirectoryPath = os.getcwd()
listOfFileNames = os.listdir(currentDirectoryPath)
for name in listofFileNames:
 if ".py" in name:
 print(name)
    ....
"""