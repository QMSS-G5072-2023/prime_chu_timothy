import math

from prime_tjc2188 import prime_tjc2188

def test_is_prime():
    assert prime_tjc2188.is_prime(3) is True, "This is prime" 
    assert prime_tjc2188.is_prime(7) is True,  "This is prime"  
    assert prime_tjc2188.is_prime(6) is False, "This is not prime"  
    assert prime_tjc2188.is_prime(9) is False, "This is not prime" 