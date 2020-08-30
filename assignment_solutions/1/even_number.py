"""
Assignment 1:
 - Check is the given number is even or not.
 - Your function should return True if the number is even, False if the number is odd.
 - Name your function `is_even`

Input: An integer
Output: A boolean

Example:
 > is_even(2) == True
 > is_even(5) == False
 > is_even(0) == True
"""


def is_even(n: int) -> bool:
    # suggested solution
    """ Check if a given number is even
    Using modulo 2, and checking if the remainder is zero
    """
    return n % 2 == 0


# tests
if __name__ == '__main__':
    assert is_even(2) is True
    assert is_even(5) is False
    assert is_even(0) is True
