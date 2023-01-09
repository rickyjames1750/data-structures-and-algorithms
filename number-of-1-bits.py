"""
Number of 1 bits 

Provided an integer, find the number of 1 bits it has.

Lets look at the following example code below


"""

def one_bits(num):
    # Fill this in.
    count = 0
    
    while num > 0:
        if num & 1 == 1:
            count += 1
        num = num >> 1
    return count 

print(one_bits(23))
# 4
# 23 = 0b10111