import random  # random number generator for 'e'
import sympy  # prime generator(note that you may not have this installed, in which case, run 'pip install sympy' from your command line(or remove lines 15-17)
import math  # GCD function
from Teacher_BackgroundFunctions_CoveredInLabs import *  # Euclid's Extended Algorythm (EEA) is here, as well as
# non-critical but still used functions, such as TextToInt, IntToText, and Padding
import hashlib  # contains hashing algorythm to be used for digital signature & checking


# This File contains a complete RSA class & associated functions, and Hashing based Signature generation and checks.
# (for the digital signature functions, see lines 83+)


# An example of how RSA could be implemented. The Class handles generating keys, while a series of functions perform
# the encryption and decryption process. The outside functions could also be implemented into the class, or the class
# could be broken up into a series of functions instead.
class KeyGeneration:
    """ p and q must be primes, or both 0 for auto-generation\n
    If you think there's an issue, try increasing the size of your factors"""

    def __init__(self, p, q):
        while p == q:  # if you didn't provide p or q, they're generated for you
            p = sympy.randprime(10**100, 20**100)  # the particular range is arbitrary, feel free to change
            q = sympy.randprime(10**100, 20**100)  # p and q are used, but not saved
        self.n = p * q  # 'n' is public, and easy to make.
        φ_n = (p-1) * (q-1)  # this one stays hidden for internal use when generating the keys, and isn't saved
        self.e = random.randint(3, φ_n - 1)  # e is also public.
        while math.gcd(self.e, φ_n) != 1:  # keep looping until there's no common factors(they'd then be co-primes)
            # if we get in the loop, the random e we chose didn't work, we need to find a new one.
            self.e = random.randint(3, φ_n - 1)

        self.__d = pow(self.e, -1, mod=φ_n)  # pow calculates the modular inverse of e (with mod φ_n), the private key 'd'
            # see https://docs.python.org/3.10/library/functions.html#pow for documentation of pow's ability to calculate Modular Inverses

    def getPrivateKey(self):
        """in the form 'd, n'. \n
        This also destroys the private key stored here, so only one person can have it"""
        d, self.__d = self.__d, "Private Key Already taken"
        return d, self.n

    def getPublicKey(self):
        """in the form 'e, n'"""
        return self.e, self.n

    def __str__(self):  # status check
        return str(f"n = {self.n}\n"
                   f"d = {self.__d}\n"
                   f"e = {self.e}")


# general RSA Encrypt/Decrypt, called on and formatted in other functions
def RSA_Method(message, type, n):
    """Requires Public or Private key part in 'type' \n
    Better to call under RSA_Encrypt or RSA_Decrypt\n
    returns integer = m^type mod n """
    return pow(message, type, n)  # all RSA en/decryption takes the form (a^b mod n) = output


def RSA_Encrypt(message, Encrypt_Key):
    """Enter a message(int or string) to be ciphered, along with the two part key to cipher with."""
    if isinstance(message, str):  # if you put a string in, we turn it into an integer first
        message = TextToInt(message)
    if message > Encrypt_Key[1]:  # if your message is larger than your modulus(n), you will lose information, corrupting your message
        raise BaseException(f"Try again, your message is too large or n is too small\n"
                            f"message = {message}\n"
                            f"n is    = {Encrypt_Key[1]}\n"
                            f"Or split the message into smaller pieces and send it in packets\n")
    return RSA_Method(message, Encrypt_Key[0], Encrypt_Key[1])


def RSA_Decrypt(ciphered_message, Decrypt_Key):
    """Inverts the operation performed by the Encryption Key\n
    Returns as string, if you want an Integer use RSA_Decrypt_Integer"""
    # RSA_Method returns the integer form of our message, so we quickly convert it back into a string before returning it
    integer_message = RSA_Method(ciphered_message, Decrypt_Key[0], Decrypt_Key[1])
    string_message = IntToText(integer_message)
    return string_message


def RSA_Decrypt_Integer(ciphered_message, Private_Key):
    """if you want the deciphered integer before it's converted into it's text value, use this function"""
    return RSA_Method(ciphered_message, Private_Key[0], Private_Key[1])

###
# Functions bellow are for Hashing as a Signature:
###
# (CHF Stands for Cryptographic Hashing Function, a subset of normal Hashing Functions useful in Cryptography)


def signed_message(message):
    """input a string message, Returns message and CHF value(as an integer)"""
    return message, Hashing(message)


def Hashing(message):
    """ This is used to turn a string into an integer CHF value"""
    bite_string = message.encode('utf-8')  # the hashing function only accepts bite based strings.
    hex_hash = "0x" + hashlib.sha256(bite_string).hexdigest()  # hashes the bite string using sha256(a CHF logarithm) and returns a hex one
    int_hash = int(hex_hash, 16)  # converts hash from hex (noted as base 16) into int for Encryption.
    return int_hash


# The previous two generate Hashing function values, while the third verifies equivalence

def SigningVerify(message, Signature, Their_Public_key):
    """Message as a string, Signature, and a Public_key as [e, n]\n
    Returns True if Signature matches, False otherwise"""
    message_hash = Hashing(message)  # rebuilding what the sender's Hash was
    HashCheck = pow(Signature, Their_Public_key[0], Their_Public_key[1])  # s^e (mod n) will equal the hash, following s^e ≡ (h^e)^d mod (n) = h
    return message_hash == HashCheck