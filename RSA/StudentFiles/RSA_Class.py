import random  # random number generator for 'e': random.random(lower-bound, upper-bound) -- This is inclusive
# https://docs.python.org/3/library/random.html#random.randint
import math  # GCD function: math.gcd(<comparable values>) --returns GCD
# https://docs.python.org/3/library/math.html#math.gcd

# For finding a Modular Multiplicative Inverse, use pow(<number to find MMI of>, -1, <modulus>)

class RSA_KeyGeneration:
    def __init__(self, p, q):
        """assume p and q are distinct primes"""


    def getPrivateKey(self):
        return None
    def getPublicKey(self):
        return None

if __name__ == "__main__":
    p = 47
    q = 73

    keygen = RSA_KeyGeneration(p, q)
    # generate the necessary keypair values here, using the RSA_KeyGeneration class's initialization

    message = 13

    # Use the RSA encryption method to cipher and then decipher a message.
    encrypted_message = cipher_function(message, )
    # this ciphered message is then transferred over a secure, but not necessarily private, connection
    decrypted_message = decipher_function(encrypted_message, )


    if message == decrypted_message:
        print("Your message has been successfully transferred!")
    else:
        print("There's an issue!")