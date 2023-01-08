"""
H-Index 

The h-index is a metric that attempts to measure the productivity and citation impact of the publication of a scholar. 
The definition of the h-index is if a scholar has at least h of their papers cited h times. 

Given a list of publications of the number of citations a scholar has, find the their h-index.

Example: 
Input: [3, 5, 0, 1, 3]
Output: 3


Explanation: 

There are 3 publications with 3 or more citations, hence the h-index is 3.

Here's a starting point: 

"""

def hIndex(publications):
    # Gets the len of how many publications they have
    n = len(publications)
    # Creates our citation array with adding one more spot to it since starting at zero 
    citations = [0] * (n + 1)

    # Looping through the publications 
    for pub in publications:
        if pub < n:
            citations[pub] += 1
        else: 
            citations[n] += 1
    
    # Start at zero to iterate from right to left 
    total = 0
    i = n
    while i >= 0:
        total += citations[i]
        # If the total is greater than the index then we just return i 
        if total >= i:
            return i
        i -= 1
    return i


print (hIndex([5, 3, 3, 1, 0]))
# 3