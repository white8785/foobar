from math import sqrt


"""
Confirms an integer is not a negative number.
"""


def is_positive(value):
    return False if value < 0 else True


"""
Given a range generate, and return a list of prime numbers
"""


def generate_primes(number):
    """
    Generate a list of prime numbers using Sieve of Eratosthenes up to, and including
    the {number} argument.

    :param number: int
    :param context: The upper limit of the prime generation range.
    :return: An array of prime integers.
    :rtype: list
    """

    # data validatiion
    if not is_positive(number):
        raise ValueError("Negative integers are not supported.")

    if number <= 3:
        raise ValueError("The number must be >= 4.")

    # Optimization_1: prepopulated array to faciliate the Sieve method
    is_prime = [True] * (number + 1)

    # special use cases
    is_prime[0] = False
    is_prime[1] = False

    start = 2
    for count1 in range(start, number):
        if is_prime[count1]:
            for count2 in range(
                count1 ** 2, number, count1
            ):  # Optimization_2: check above root of n
                is_prime[count2] = False

    primes = [prime for prime in range(number) if is_prime[prime]]
    return primes


"""
Required function and spec for the system

int i a number between 0 - 10000

:returns: 5 character string Id
"""


def solution(i):
    """
    Given index (i), return string of digits starting with i as index
    from a string of prime numbers.
    """
    # data validation
    if not i >= 0 and i <= 10000:
        raise ValueError("Your number is out of range")

    range = i + 5
    primes = generate_primes(30000)

    string_of_primes = ""
    for prime in primes:
        string_of_primes += str(prime)

    return string_of_primes[i:range]


"""
Local dev only
"""
if __name__ == "__main__":
    assert is_positive(2) == True
    assert is_positive(-1) == False

    # id = solution(10000)
    for i in range(9995, 10000):
        id = solution(i)
        print(id)
