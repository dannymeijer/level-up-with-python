from typing import Iterable


def remove_all_before(items: list, border: int) -> Iterable:
    """ Remove from the list all of the elements before the given one

    For example:
    For the illustration we have a list [3, 4, 5] and we need to remove
    all elements that go before 3 - which is 1 and 2.

    We have two edge cases here:
     1. if a cutting element cannot be found, then the list should
        not be changed;
     2. if the list is empty, then it should remain empty;

    Input: List and the border element.
    Output: Iterable (tuple, list, iterator ...).

    Usage example:
    remove_all_before([1, 2, 3, 4, 5], 3) == [3, 4, 5]
    remove_all_before([1, 1, 2, 2, 3, 3], 2) == [2, 2, 3, 3]

    """
    # handle edge cases
    # - if the list is empty, then it should remain empty
    if len(items) == 0:
        return []
    # - if a cutting element cannot be found, then the list should
    #   not be changed
    elif border not in items:
        return items

    # find index of border, slice it, and return
    else:
        return items[items.index(border):]


def remove_all_before_shorter(items: list, border: int) -> Iterable:
    """ Shorter alternative to remove_all_before"""
    return (
        # if the list is empty, it remains empty
        [] if len(items) == 0
        # if a cutting element cannot be found, the list is not changed
        else items if border not in items
        # else find index of border, slice it, and return
        else items[items.index(border):]
    )


if __name__ == "__main__":
    print("Example:")
    print(list(remove_all_before([1, 2, 3, 4, 5], 3)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(remove_all_before([1, 2, 3, 4, 5], 3)) == [3, 4, 5]
    assert list(remove_all_before([1, 1, 2, 2, 3, 3], 2)) == [2, 2, 3, 3]
    assert list(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)) == [2, 4, 2, 3, 4]
    assert list(remove_all_before([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
    assert list(remove_all_before([], 0)) == []
    assert list(remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [7, 7, 7, 7, 7, 7, 7, 7, 7]
    print("Coding complete? Click 'Check' to earn cool rewards!")
