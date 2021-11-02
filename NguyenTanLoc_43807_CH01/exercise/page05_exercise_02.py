"""
Author: Nguyen Tan Loc
Date: 25/08/2021
Problem: Write an algorithm that describes the second part of the process of making change
(counting out the coins and bills)
Solution: example, if you buy a dozen eggs at the farmers’ market for $2.39 and you give the farmer a
$10 bill, she should return $7.61 to you. To produce this amount, the merchant selects the
appropriate coins and bills that, when added to $2.39, make $10.00.
According to another method, the merchant starts with the purchase price and goes toward
the amount given. First, coins are selected to bring the price to the next dollar amount (in
this case, $0.61 3 5 dimes, 1 nickel, and 4 pennies), then dollars are selected to bring the
price to the next 5-dollar amount (in this case, $2), and then, in this case, a $5 bill completes
the transaction

"""