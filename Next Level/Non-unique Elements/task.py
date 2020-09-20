"""
f you have 50 different plug types, appliances wouldn't be available and would
be very expensive. But once an electric outlet becomes standardized, many
companies can design appliances, and competition ensues, creating variety and
better prices for consumers.
-- Bill Gates

You are given a non-empty list of integers (X). For this task, you should
return a list consisting of only the non-unique elements in this list. To do
so you will need to remove all unique elements (elements which are contained
in a given list only once). When solving this task, do not change the order
of the list. Example: [1, 2, 3, 1, 3] 1 and 3 non-unique elements and result
will be [1, 3, 1, 3].

non-unique-elements
Input: A list of integers.

Output: An iterable of integers.

Example:
non_unique_elements([1, 2, 3, 1, 3]) == [1, 3, 1, 3]
non_unique_elements([1, 2, 3, 4, 5]) == []
non_unique_elements([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]
non_unique_elements([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9]
non_unique_elements([2]) == []

How it is used: This task will help you to understand how to manipulate
arrays, something that is the basis for solving more complex tasks. The
concept can be easily generalized for real world tasks. For example: if you
need to clarify statistics by removing low frequency elements (noise).
"""


def non_unique_elements(data: list) -> list:
    ...


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(non_unique_elements([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(non_unique_elements([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(non_unique_elements([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(non_unique_elements([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
