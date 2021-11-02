"""
Author: Nguyen Tan Loc
Date: 1/09/2021
Problem: An employee’s total weekly pay equals the hourly wage multiplied by the total
number of regular hours plus any overtime pay. Overtime pay equals the total
overtime hours multiplied by 1.5 times the hourly wage. Write a program that
takes as inputs the hourly wage, total regular hours, and total overtime hours and
displays an employee’s total weekly pay
Solution:

"""
# Request the inputs le fivestar.py
wage = float(input("Enter the wage: $"))
regularHours = float(input("Enter the regular hours: "))
overtimeHours = float(input("Enter the overtime hours: "))
# Compute the result
totalPay = regularHours * wage + overtimeHours * wage * 1.5
# Display the result
print("The total weekly pay is $" + str(round(totalPay, 2)))


