def end_zeros(num: int) -> int:
    """ find out how many zeros a given number has at the end 
    How it works:
    -------------
    Find the first non-zero while looping to the inverse string 
     representation of the number
    """
    zero_count = 0
    for c in str(num)[::-1]:  
        if c != "0":
            break
        zero_count += 1
    return zero_count


if __name__ == '__main__':
    print("Example:")
    print(end_zeros(0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")
