"""
Author: Nguyen Tan Loc
Date: 7/10/2021
Problem:Write a recursive function that expects a pathname as an argument. The pathname can be either the name of a file or the name of a directory. If the pathname
refers to a file, its name is displayed, followed by its contents. Otherwise, if the
pathname refers to a directory, the function is applied to each name in the directory. Test this function in a new program.
Solution:


    ....
"""
import os
import os. path

def main():

    displayFiles(os.getcwd())

def displayFiles(path):

    if os. path.isfile(path):
        print("File name: " + path)
        f = open(path, 'r')
        print(f.read())
    else:
        print("Directory name: " + path)
        Lyst = os.listdir(path)
        for element in Lyst:
            recursive_element = os.path.john(path, element)
            print("element:", element)
            print("recursive_element:",recursive_element)
            displayFiles (recursive_element)
if __name__== 'main':
    print(f"Directory : {os.getcwd()}")
    displayFiles(os.getcwd())