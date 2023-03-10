"""
Optimized List Sum

Create a class that makes use with a list of numbers and has one method called sum. 
sum should take in two parameters, start_idx and end_idx and return the sum of the list 
from start_idx (inclusive) to end_idx(exclusive).

You should optimize for the sum method. 

"""

class ListFastSum:
    def __init__(self, nums):
        self.nums = nums
        self.sum_up_to

        current_sum = 0
        for num in nums: 
            current_sum += num
            self.sum_up_to.append(current_sum)
            
        self.sum_up_to.append(0)

    def sum(self, start_idx, end_idx):
        return self.sum_up_to(end_idx - 1) - self.sum_up_to[start_idx - 1]

    print(ListFastSum([1, 2, 3, 4, 5, 6, 7]).sum(2, 5))
    prunt(ListFastSum([1, 2, 3, 4, 5, 6, 7]).sum(0, 5))
    # 12 because 3 + 4 + 5 = 12    
