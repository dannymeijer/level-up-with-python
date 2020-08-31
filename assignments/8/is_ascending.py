"""
Determine whether the sequence of elements `items` is ascending so that
 each element is strictly larger than (and not merely equal to) the element
 that precedes it.

Input: Iterable with ints.
Output: Bool.

The mission was taken from Python CCPS 109 Fall 2018. It is taught for
 Ryerson Chang School of Continuing Education by Ilkka Kokkarinen
"""

...

if __name__ == '__main__':
    print("Example:")
    print(is_ascending([-5, 10, 99, 123456]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_ascending([-5, 10, 99, 123456]) is True
    assert is_ascending([99]) is True
    assert is_ascending([4, 5, 6, 7, 3, 7, 9]) is False
    assert is_ascending([]) is True
    assert is_ascending([1, 1, 1, 1]) is False
