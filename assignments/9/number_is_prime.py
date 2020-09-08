"""
Your goal is to write a program to check if a number is prime or not

As a reminder:
 - Primes are a positive integer greater than 1 which has no other factors
    except 1 and the number itself: e.g. 2, 3, 5, 7 ... are prime numbers as
    they do not have any other factors. But 6 is not prime (it is composite)
    since, 2 x 3 = 6.

Input: any positive integer
Output: a boolean stating if the given number is prime or not
Bonus: have the function print why a number is prime or not
"""
...  # your code goes here

if __name__ == '__main__':
    print(is_prime(407))

    # Test cases
    assert is_prime(407) is False
    assert is_prime(2) is True
    assert is_prime(821) is True
    assert is_prime(613) is True
    assert is_prime(612) is False
    assert is_prime(7) is True
