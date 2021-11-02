"""
Author: Nguyen Tan Loc
Date: 10/09/2021
Problem:
The credit plan at TidBit Computer Store specifies a 10% down payment and
an annual interest rate of 12%. Monthly payments are 5% of the listed purchase
price, minus the down payment. Write a program that takes the purchase price
as input. The program should display a table, with appropriate headers, of a payment schedule for the lifetime of the loan. Each row of the table should contain
the following items:
• the month number (beginning with 1)
• the current total balance owed
• the interest owed for that month
• the amount of principal owed for that month
• the payment for that month
• the balance remaining after payment
The amount of interest for a month is equal to balance * rate / 12. The amount of
principal for a month is equal to the monthly payment minus the interest owed.
Solution:

"""

price = float(input("Total computer cost:"))
initialprice=price
remaining_price = (price * 0.9)

monthly_payment = remaining_price * 0.05

interest_owed = remaining_price * (.12/12.0)

principal = monthly_payment - interest_owed

month = 0
print("Month Starting Balance Intrest_owed Principal To pay Payment Ending Balance")

while remaining_price > 0:
    month += 1
    remaining_price -= principal
    interest_owed = remaining_price * (.12/12.0)
    principal = monthly_payment - interest_owed

    print('{:} {:>12.2f} {:>17.2f} {:>12.2f} {:>12.2f} {:>17.2f}'.format(month, initialprice, interest_owed, principal, monthly_payment, remaining_price))
    initialprice=remaining_price

