"""
Assignment 2:
 - You have a positive integer.
 - Try to find out how many digits it has.
 - Name the function "number_of_digits"

Input: A positive Int
Output: An Int.

For example:
 > number_of_digits(10) would return 2

"""


...


# tests
if __name__ == '__main__':
    assert number_of_digits(10) == 2
    assert number_of_digits(0) == 1
    assert number_of_digits(4) == 1
    assert number_of_digits(44) == 2
    assert number_of_digits(123) == 3
