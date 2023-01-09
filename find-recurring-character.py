"""
Find reccurring character 

Provided  a string, return the first recurring letter that appears. If there are no recurring letters, return None.

Examle below:

Example: 

Input: qwertty
Output: t

Input: qwerty
Output: None 

"""

def first_recurring_char(s):
    seen_so_far = set()

    for c in s:
        if c in seen_so_far:
            return c
        seen_so_far.add(c)
    # Else return none 
    return None

print(first_recurring_char("qwertty"))
# t

print(first_recurring_char("qwerty"))
# None 