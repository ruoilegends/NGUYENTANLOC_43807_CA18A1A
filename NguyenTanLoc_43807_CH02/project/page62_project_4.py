"""
Author: Nguyen Tan Loc
Date: 1/09/2021
Problem: Write a program that takes the radius of a sphere (a floating-point number) as
input and then outputs the sphere’s diameter, circumference, surface area, and
volume.
Solution:
5

"""
import math
# Request the input
radius = float(input("Enter the sphere's radius: "))
# Compute the results
diameter = 2 * radius
circumference = diameter * math.pi
surfaceArea = 4 * math.pi * radius * radius
volume = 4 / 3.0 * math.pi * radius * radius * radius
# Display the results
print("Diameter :", diameter)
print("Circumference:", circumference)
print("Surface area :", surfaceArea)
print("volume      :",volume)
