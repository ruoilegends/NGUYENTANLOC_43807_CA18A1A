"""
Author: Nguyen Tan Loc
Date: 15/10/2021
Problem:
 Turtle graphics windows do not automatically expand in size. What do you suppose
happens when a Turtle object attempts to move beyond a window boundary?
Solution:
About Turtle Graphics
  • A turtle graphics toolkit provides a simple and enjoyable way to draw pictures in a window and give opportunity to run several methods with an object.
  • To use turtle object in a program the below steps should be followed
1. Importing class from package
  • Turtle class should be imported form "turtle" package. This can be achieved using the statement from turtle import Turtle
2. Object Instantiation
  • To perform any kind of Operating using turtle an object of Turtle class that has been imported in the previous statement should be created. This can be achieved using the statement t=Turtle()
  • The variable holding the instance of "Turtle" class can be any valid identifier.
3. Call to a method
  • Now an object that holds the instance of class "Turtle" has been created in the previous two statements.
  • Any method of turtle package can be called as follows t.method_Name() method_Name is any method of Turtle class like
   o t.up() which is used to turn the pen up
   o t.down() which is used to turn the pen down and many more.
    ....
"""