"""
Your goal is to write a program to check if a number is prime or not

As a reminder:
 - Primes are a positive integer greater than 1 which has no other factors
    except 1 and the number itself: e.g. 2, 3, 5, 7 ... are prime numbers as
    they do not have any other factors. But 6 is not prime (it is composite)
    since, 2 x 3 = 6.

Input: any positive integer
Output: a boolean stating if the given number is prime or not
Bonus: have the function print why/that a number is prime or not
"""


def is_prime(n: int) -> bool:
    """ Simple function to check if a given number n is prime or not

    Parameters
    ----------
    n: int
        number that will be checked if it is prime or not

    Returns
    -------
    bool: True if the given number (n) is prime, False if it is not

    """
    while True:
        if n <= 1:  # prime numbers are greater than 1
            prime, i = False, 1

        else:
            for i in range(2, n):  # Iterate from 2 to n / 2
                # If n is divisible by any number between 2 and n / 2,
                #  it is not prime
                if n % i == 0:
                    prime = False
                    break
            else:
                prime, i = True, 0

        if prime is not None:
            break

    print(
        f"'{n}' is a prime number" if prime
        else f"'{n}' is not a prime number, it is divisible by {i}",
    )
    return prime


if __name__ == "__main__":
    # Test cases
    assert is_prime(407) is False
    assert is_prime(1) is False
    assert is_prime(2) is True
    assert is_prime(821) is True
    assert is_prime(613) is True
    assert is_prime(612) is False
    assert is_prime(7) is True
    assert is_prime(991) is True
