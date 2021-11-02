"""
Author: Nguyen Tan Loc
Date: 10/09/2021
Problem:  Teachers in most school districts are paid on a schedule that provides a salary
based on their number of years of teaching experience. For example, a beginning
teacher in the Lexington School District might be paid $30,000 the first year. For
each year of experience after this first year, up to 10 years, the teacher receives a
2% increase over the preceding value. Write a program that displays a salary schedule, in tabular format, for teachers in a school district. The inputs are the starting
salary, the percentage increase, and the number of years in the schedule. Each row
in the schedule should contain the year number and the salary for that year.
Solution:

"""
startingSalary= int(input("Please Enter starting salary: ")) # Reading Starting salary
perIncrease= int(input("Please Enter annual percentage increase: ")) # Reading annual increase
noOfYears= int(input("Please Enter number of years: "))#reading number of years
print("Salaries starting from first year are:")
print(startingSalary)
for i in range(noOfYears - 1): # iteration for getting next year's salary
    n = startingSalary * perIncrease/100
    startingSalary += n #adding to previous year's salary
    print(startingSalary) #printing salary

