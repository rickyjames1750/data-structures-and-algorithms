"""

Determind if number 

Given a string that may represent a number, determine if it is a number.
Here's some of examples of how the number may be presented:

"123"    # Integer
"12.3"   # Floating point 
"-123"   # Negative numbers
"-.3"    # Negative floating point 
"1.5e5"  # Scientific notation

Here's some examples of what isn't a proper number:
"12a"    # No letters
"1 2"    # No space between numbers 
"1e1.2"  # Exponent can only be an integer (positive or negative or 0)

Scientic notation requires the first number to be less than 10, however to simplify
the solution assume the first number can be greater than 10. Do not parse the string
with int() or any other python functions. 

"""

