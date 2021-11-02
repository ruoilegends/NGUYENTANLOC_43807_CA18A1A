"""
Author: Le Van The
Date: 23/10/2021
Problem:
Add a command to this chapter’s case study program that allows the user to
view the contents of a file in the current working directory. When the command
is selected, the program should display a list of filenames and a prompt for the
name of the file to be viewed. Be sure to include error recovery.
Solution:


    ....
"""
import os, os.path
QUIT = '8'
COMMANDS = ('1', '2', '3', '4', '5', '6', '7','8')
MENU = """1 List the current directory
2 Move up
3 Move down
4 Number of files in the directory
5 Size of the directory in bytes
6 Search for a filename
7 View the contents of a file
8 Quit the program"""

def acceptCommand():
    """Inputs and returns a legitimate command number."""
    while True:
        command = str(input("Enter a number: "))
        if command in COMMANDS:
            print("Error: command not recognized")

        else:
            return command

def runCommand(command):
    """Selects and runs a command."""
    if command == '1':
        print("call listCurrentDir")
        listCurrentDir(os.getcwd())
    elif command == '2':
        print("call moveUp")
        moveUp()
    elif command == '3':
        print("call moveDown")
        moveDown(os.getcwd())
    elif command == '4':
        print("The total number of files is", \
        countFiles(os.getcwd()))
    elif command == '5':
        print("The total number of bytes is", \
        countBytes(os.getcwd()))
    elif command == '6':
        target = input("Enter the search string: ")
        fileList = findFiles(target, os.getcwd())
        if not fileList:
            print("String not found")
        else:
            for f in fileList:
                print(f)()
    elif command == '7':
        print("call viewFile")
        viewFile(os.getcwd())

def viewFile (dirName):
    lyst = list(filter(os.path.isfile, os.listdir(dirName)))
    if len(lyst) == 0:
        print("There are no files in this directory")
    else:
        while True:
            print("Files in " + dirName + ":")
            for element in lyst: print(element)
            fileName = input("Enter a file name from these names: ")
            if not fileName in lyst:
                print("Sorry, there is an error in your file name.")
            else:
                f = open(fileName, 'r')
                print(f.read ())
                break


def listCurrentDir(dirName):
    """Prints a list of the cwd's contents."""
    lyst = os.listdir(dirName)
    for element in lyst:
        print(element)

def moveUp():
    """Moves up to the parent directory."""
    os.chdir("..")

def moveDown(currentDir):
    """Moves down to the named subdirectory if it exists."""
    newDir = input("Enter the directory name: ")
    if os.path.exists(currentDir + os.sep + newDir) and \
       os.path.isdir(newDir):
       os.chdir(newDir)
    else:
       print("ERROR: no such name")

def countFiles(path):
    """Returns the number of files in the cwd and
    all its subdirectories."""
    count = 0
    lyst = os.listdir(path)
    for element in lyst:
        if os.path.isfile(element):
           count += 1
        else:
           os.chdir(element)
           count += countFiles(os.getcwd())
           os.chdir("..")
    return count

def countBytes(path):
    """Returns the number of bytes in the cwd and
    all its subdirectories."""
    count = 0
    lyst = os.listdir(path)
    for element in lyst:
        if os.path.isfile(element):
           count += os.path.getsize(element)
        else:
           os.chdir(element)
           count += countBytes(os.getcwd())
           os.chdir("..")
    return count

def findFiles(target, path):
    """Returns a list of the filenames that contain
    the target string in the cwd and all its subdirectories."""
    files = []
    lyst = os.listdir(path)
    for element in lyst:
        if os.path.isfile(element):
           if target in element:
              files.append(path + os.sep + element)
           else:
              os.chdir(element)
              files.extend(findFiles(target, os.getcwd()))
              os.chdir("..")
    return files

if __name__ == "_main_":
    while True:
        print(os.getcwd())
        print(MENU)
        command = acceptCommand()
        runCommand(command)
        if command == QUIT:
            print("Have a nice day!")
            break