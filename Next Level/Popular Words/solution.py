from typing import List, Dict
from textwrap import dedent


def popular_words(text: str, words: List[str]) -> Dict[str, int]:
    """determine the popularity of certain words in the text

    Input consists of 2 arguments: the text and the array of words the
     popularity of which is determined.

    The words are sought in all registers. This means that if you need to
     find a word "one" then words like "one", "One", "oNe", "ONE" etc. will do.
    If the word was not found even once, the dictionary will report a 0 (zero).

    Input: The text and the search words array.
    Output: The dictionary where the search words are the keys and values are
     the number of times when those words are occurring in a given text.
    """
    # To enable `search in all registers`, everything is lowercase
    bag_o_words = text.lower().split()
    return {  # search results per word
        word: bag_o_words.count(word) for word in words
    }


if __name__ == "__main__":
    print("Example:")
    print(
        popular_words(
            dedent("""
            When I was One
            I had just begun
            When I was Two
            I was nearly new
            """),
            ["i", "was", "three", "near"],
        )
    )

    # These "asserts" are used for self-checking and not for an auto-testing
    assert (
        popular_words(
            dedent("""
            When I was One
            I had just begun
            When I was Two
            I was nearly new
            """),
            ["I", "was", "three", "near"],
        )
        == {"i": 4, "was": 3, "three": 0, "near": 0}
    )
    print("Coding complete? Click 'Check' to earn cool rewards!")
