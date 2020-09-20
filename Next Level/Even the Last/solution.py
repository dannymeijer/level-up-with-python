def is_even(x: int):
    """ returns True if x is even, False if odd """
    return x % 2 == 0


def even_the_last(array: list) -> int:
    """
        sums even-indexes elements and multiply at the last
    """
    if array:
        even_index_numbers = [num for i, num in enumerate(array) if is_even(i)]
        return sum(even_index_numbers) * array[-1]
    else:
        return 0


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(even_the_last([0, 1, 2, 3, 4, 5]))
    
    assert even_the_last([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert even_the_last([1, 3, 5]) == 30, "(1+5)*5=30"
    assert even_the_last([6]) == 36, "(6)*6=36"
    assert even_the_last([]) == 0, "An empty array = 0"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
