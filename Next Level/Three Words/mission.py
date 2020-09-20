def has_three_words(words: str) -> bool:
    bag_o_words, counter = words.split(), 0
    for word in bag_o_words:
        counter = 0 if not word.isalpha() else counter + 1
        if counter == 3:
            return True
    else:
        return False


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(has_three_words("Hello World hello"))
    
    assert has_three_words("Hello World hello") is True, "Hello"
    assert has_three_words("He is 123 man") is False, "123 man"
    assert has_three_words("1 2 3 4") is False, "Digits"
    assert has_three_words("bla bla bla bla") is True, "Bla Bla"
    assert has_three_words("Hi") is False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
