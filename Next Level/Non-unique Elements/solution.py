def non_unique_elements(data: list) -> list:
    return [x for x in data if data.count(x) > 1]


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(non_unique_elements([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(non_unique_elements([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(non_unique_elements([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(non_unique_elements([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
