"""

Check for palindrome 

Provided a string, determine if there is a way to arrange the string
such that the string is a palidrome. If such arrangement exists, return
a palidrome (There could be many arrangments).

Otherwise return None.

"""
from collections import defaultdict

def find_palindrome(s):
    char_count = defaultdict(int)

    for c in s:
        char_count[c] += 1

    odd_char = ""
    palindrome = ""

    for c, cnt in char_count.items():
        if cnt % 2 == 0:
            palindrome += c * (cnt//2)
        elif not odd_char:
            odd_char = c
            palindrome += c * (cnt//2)
        else:
            return None

    return palindrome + odd_char + palindrome[::-1]


print(find_palindrome('momom'))
# mommom
print(find_palindrome('qqaaaao'))
# None


