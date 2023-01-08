"""
Disburse Bonus Pay! 

Lets say you are the manager of a number of workers who all sit in a row. 
The C.E.O. would like tp give bonuses to all of your workers, 
but since the Startup did not perform so well this year the CEO would like to keep bonuses to a minumum. 

The rules of disbursing the bonuses is: 
- Each Worker starts with a bonus factor of 1x. 
- For each worker, if they perform better than the person sitting next to them, 
the worker is given +1 higher bonuses ( and up to +2 if they performn better than both people to their sides).

Provided a list of worker's performance, locate the bonuses each worker should get.

Example: 
Input: [1, 2, 3, 2, 3, 5, 1]
Output: [1, 2, 3, 1, 2, 3, 1]

Here's the starting point: 

"""

def getBonuses(performance):

print(getBonuses([1, 2, 3, 2, 3, 5, 1]))
# [1, 2, 3, 1, 2, 3, 1]