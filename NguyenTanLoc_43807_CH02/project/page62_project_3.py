"""
Author: Nguyen Tan Loc
Date: 1/9/2021
Problem: Five Star Retro Video rents VHS tapes and DVDs to the same connoisseurs who
like to buy LP record albums. The store rents new videos for $3.00 a night, and
oldies for $2.00 a night. Write a program that the clerks at Five Star Retro Video
can use to calculate the total charge for a customer’s video rentals. The program
should prompt the user for the number of each type of video and output the total
cost
Solution:

"""
# Initialize constants
NEW_RENTAL = 3.00
OLDIE_RENTAL = 2.00
# Request the inputs
newones = int(input("Enter the number of new videos: "))
oldones = int(input("Enter the number of oldies: "))
# Compute the results
totalCost = NEW_RENTAL * newones + OLDIE_RENTAL * oldones
# Display the results
print("The total cost is $" + str(round(totalCost, 2)))
