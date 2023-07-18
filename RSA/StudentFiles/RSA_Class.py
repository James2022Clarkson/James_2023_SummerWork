import random  # random number generator for 'e': random.random(lower-bound, upper-bound) -- This is inclusive
# https://docs.python.org/3/library/random.html#random.randint
import math  # GCD function: math.gcd(<comparable values>) --returns GCD
# https://docs.python.org/3/library/math.html#math.gcd

# For finding a Modular Multiplicative Inverse, use pow(<number to find MMI of>, -1, mod=modulus)

# This file implements a RSA Class in a basic format, and does not include any safeguards or additional usages.
# For some details on the why and how, see ###POWERPOINT###


class KeyGeneration:
    def __init__(self, p, q):
        """ p and q must be distinct primes"""
        self.n = p * q
        φ_n = (p - 1) * (q - 1)
        self.e = 2**4 + 1
        while math.gcd(self.e, φ_n) != 1:
            self.e = random.randint(3, φ_n - 1)
        self.d = pow(self.e, -1, mod=φ_n)

    def getPrivateKey(self):
        """in the form (d, n)"""
        return self.d, self.n

    def getPublicKey(self):
        """in the form (e, n)"""
        return self.e, self.n


def RSA_Method(message, key):
    """Requires Public or Private key\n
    returns (message^key[0]) mod key[1])\n
    Formatted to work with getKey Functions """
    return pow(message, key[0], key[1])
