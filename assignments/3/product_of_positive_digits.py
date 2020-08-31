"""
Assignment 3:
 - You are given a positive integer.
 - Your function should calculate the product of the digits excluding any zeroes.
 - Name the function "product_of_positive_digits"

Input: A positive integer.
Output: The product of the digits as an integer.

For example:
 > The number given is 123405.
 > The result will be 1*2*3*4*5=120 (don't forget to exclude zeroes).

Hint: use the math library
"""

...

# tests
if __name__ == '__main__':
    assert product_of_positive_digits(123405) == 120
    assert product_of_positive_digits(999) == 729
    assert product_of_positive_digits(1000) == 1
    assert product_of_positive_digits(1111) == 1
