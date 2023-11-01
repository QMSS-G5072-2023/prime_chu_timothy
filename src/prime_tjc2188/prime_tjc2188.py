import math

"""
    Returns True if intiger is prime and False if intiger is not prime.

    Parameters
    ----------
    n: intiger

    Returns
    -------
    True
    False
    
    Examples
    --------
    >>> from prime_tjc2188 import prime
    >>> n = 5
    >>> prime_tjc2188.prime(n)
    True    
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


