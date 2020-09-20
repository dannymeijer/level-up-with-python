def is_even(x: int):
    """ returns True if x is even, False if x is odd """
    return x % 2 == 0


def even_times_last(array: list) -> int:
    """ sums even-indexes elements, multiplied with the last digit
    - Most readable solution
    """
    # empty array returns 0
    if len(array) == 0:
        return 0
    else:
        # sum all integers at even indexes, multiply with the final element
        even_index_numbers = [num for i, num in enumerate(array) if is_even(i)]
        final_element = array[-1]
        return sum(even_index_numbers) * final_element


def even_times_last_shorter(array: list) -> int:
    """ sums even-indexes elements, multiplied with the last digit
    - Most concise solution
    """
    return (
        # empty array returns 0
        0 if len(array) == 0
        # sum all integers at even indexes, multiply with the final element
        else sum([num for i, num in enumerate(array) if is_even(i)]) * array[-1]
    )


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    print("Example:")
    print(even_times_last([0, 1, 2, 3, 4, 5]))

    assert even_times_last([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert even_times_last([1, 3, 5]) == 30, "(1+5)*5=30"
    assert even_times_last([6]) == 36, "(6)*6=36"
    assert even_times_last([]) == 0, "An empty array = 0"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
