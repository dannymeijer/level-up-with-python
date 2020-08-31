"""
How old are you in a number of days?
It's easy to calculate - just subtract your birthday from today.

We could make this a real challenge though and count the difference between
 any two dates.

Assignment 5:
 - You are given two dates as a tuple with three numbers - year, month and day.
   For example: 19 April 1982 will be (1982, 4, 19).
 - You should find the difference in days between the given dates.
   For example: between today and tomorrow = 1 day.
 - The difference will always be either a positive number or zero, so don't
   forget about the absolute value. Meaning: the order of input should make no
   difference to the outcome.

Input: Two dates as tuples of integers.
Output: The difference between the dates in days as an integer.

Example:
 > days_between((1982, 4, 19), (1982, 4, 22)) == 3
 > days_between((2014, 1, 1), (2014, 8, 27)) == 238

Hint:
Use Python's built-in datetime module

Precondition:
Dates between 1 january 1 and 31 december 9999. Dates are correct.
"""

from datetime import date


# possible solution
def days_between_a(a, b) -> int:
    dates = [a, b]
    dates.sort()
    return (date(*dates[1]) - date(*dates[0])).days


# possible solution
def days_between_b(a, b):
    return abs((date(*a) - date(*b)).days)


# tests
if __name__ == '__main__':
    days_between = days_between_a
    # days_between = days_between_b
    print(days_between((1982, 4, 19), (1982, 4, 22)))
    assert days_between((1982, 4, 19), (1982, 4, 22)) == 3

    print(days_between((1982, 4, 25), (1982, 4, 22)))
    assert days_between((1982, 4, 19), (1982, 4, 22)) == 3

    print(days_between((1900, 4, 25), (1982, 4, 22)))
    assert days_between((1900, 4, 25), (1982, 4, 22)) == 29947

    print(days_between((2019, 4, 25), (1982, 4, 22)))
    assert days_between((2019, 4, 25), (1982, 4, 22)) == 13517

    print(days_between((2019, 4, 25), (2019, 4, 25)))
    assert days_between((2019, 4, 25), (2019, 4, 25)) == 0

    print(days_between((2014, 1, 1), (2014, 8, 27)))
    assert days_between((2014, 1, 1), (2014, 8, 27)) == 238
