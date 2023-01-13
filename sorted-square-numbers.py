"""

Sorted Square Numbers 

Given a list of sorted numbers (can be both negative or positive), 
return the list of numbers sqaured in sorted order. 

Here's an example and some sortinf code: 
x
"""

def sqaure_numbers(nums):
    # Fill this line with code 
    negative_stack = []

    result = []
    for n in nums:
        if n < 0:
            negative_stack.append(n)
            continue
    while len(negative_stack) > 0 and -negative_stack[-1] <= n:
        result.append(negative_stack.pop()**2)

    result.append(n**2)


    while len(negative_stack) > 0:
        result.append(negative_stack.pop()**2)


    return result


print(sqaure_numbers([-5, -3, -1, 0, 4, 5]))
print(sqaure_numbers([-10, -9, -4, -2, -1, -1, -1]))
print(sqaure_numbers([1, 2, 3, 4, 4, 4, 5]))
print(sqaure_numbers([-7, -3, -1, 0, 4, 5]))
# [0, 1, 1, 9, 16, 25, 25]

