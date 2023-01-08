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
    # Count how many workers there are 
    count = len(performance)
    # Bonus array and init 1 
    bonus = [1] * count

    # Now lets go from left to right 
    # Start at 1 becuase if we start at 0 we are not going to have anyone to our left 
    for i in range(1, count):
        # if my performance is bigger than the guy on my left then I get a bonus 
        if performance[i-1] < performance[i]:
            bonus[i] = bonus[i-1] + 1

    # Don't want to go all the way to the right or else we go out of index
    # - 1 -1 since we are going backwards 
    for i in range(count - 2, -1, -1):
        if performance[i+1] < performance[i]:
            bonus[i] = max(bonus[i], bonus[i + 1] + 1)

    return bonus

print(getBonuses([1, 2, 3, 2, 3, 5, 1]))
# [1, 2, 3, 1, 2, 3, 1]