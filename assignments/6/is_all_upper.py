import re

only_letters = re.compile("[a-zA-Z]")


...


if __name__ == '__main__':
    print("Example:")
    print(is_all_upper('ALL UPPER'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_all_upper('ALL UPPER') is True
    assert is_all_upper('all lower') is False
    assert is_all_upper('mixed UPPER and lower') is False
    assert is_all_upper('') is False
    assert is_all_upper('   ') is False
    assert is_all_upper('123') is False

    print("Coding complete? Click 'Check' to earn cool rewards!")
