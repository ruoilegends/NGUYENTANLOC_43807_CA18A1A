"""
Author: Nguyen Tan Loc
Date: 1/09/2021
Problem: You can calculate the surface area of a cube if you know the length of an edge.
Write a program that takes the length of an edge (an integer) as input and prints
the cube’s surface area as output
Solution:

"""
# Request the input
edge = float(input("Enter the cube's edge: "))
surfaceArea = edge * edge * 6
# Display the surface area
print("The surface area is", surfaceArea, "square units.")
