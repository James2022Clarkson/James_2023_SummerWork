from Teacher_PrimitiveRootsFunctions_DiffieHellmanBackgroundFunction import LeastPrimitiveRoot
# LeastPrimitiveRoot is used to find the smallest Primitive Root of the chosen Modulus

# A possible example of Diffie-Hellman's implementation as a class
# the __str__ class was added to make the demo clearer
# Several ways could be done to change this version, such as adding a 'holding' variable for the half-key in the class,
    # finding the Primitive Root in the class, or by shifting the first step into the initialization process.
class DH:
    # Diffie-hellman method
    def __init__(self, Primitive_root, prime, name):
        """Both the Primitive Root & Prime Modulus do not change, and so are declared during initialization"""
        self.generator, self.prime = Primitive_root, prime
        self.name = name  # used for print/error tracking, not used in algorithms
        self.key = None  # initializes variable for completion later

    def DH_FirstStep(self, secret_value1):
        """Initial half-key generation\n
        this is not saved as it doesn't get used in the class instance it's made in"""
        return pow(self.generator, secret_value1, mod=self.prime)  # calculates and returns half-key

    def DH_SecondStep(self, half_key, secret_value2):
        """Takes half-key and finishes it. Does not return a value"""
        self.key = pow(half_key, secret_value2, mod=self.prime)  # finished key is made and saved

    def __str__(self):  # status check of all values in the Class instance
        return f"{self.name}'s values: \n" \
               f"   Primitive Root Base:    {self.generator}\n" \
               f"   Prime Modulus:          {self.prime}\n" \
               f"   Key status:             {self.key}\n"


if __name__ == '__main__':

    # public values:
    prime = 23
    g = LeastPrimitiveRoot(prime, prints=False)  # change prints to True if you want to look into Primitive Roots

    # secret random values (must be between 1 and prime-1)
    # Note that they are only called upon by their user's class. Notice Alice calls Alice's random secret, but not Bob's
    secret_int_alice = 8
    secret_int_bob = 3

    print("Empty DH generation:")
    Alice_key = DH(g, prime, 'Alice')
    Bob_key = DH(g, prime, 'Bob')
    print(Alice_key)
    print(Bob_key)

    print("\nhalfkey generation...")
    Alices_halfkey = Alice_key.DH_FirstStep(secret_int_alice)
    Bobs_halfkey = Bob_key.DH_FirstStep(secret_int_bob)
    # this doesn't do anything to the class. we could just as easily do the math without using the class.
    print("Alice's:", Alices_halfkey)
    print("Bob's:", Bobs_halfkey)

    # the half-keys are then transferred and swapped, possibly insecurely
    print("transfering...")
    halfkey_fromBob = Bobs_halfkey  # goes to Alice
    halfkey_fromAlice = Alices_halfkey  # goes to Bob
    # names changed to indicate simulated 'transfer' and to make the further names clearer
    print("Alice now has:", halfkey_fromBob)
    print("Bob now has:", halfkey_fromAlice)

    print("\nfinished key:")
    # we don't assign the result to a value. Since we're just updating the class, the key is inside each of them
    Alice_key.DH_SecondStep(halfkey_fromBob, secret_int_alice)
    Bob_key.DH_SecondStep(halfkey_fromAlice, secret_int_bob)
    print(Alice_key)
    print(Bob_key)
    # see that 'key' now has a value

    print("\n A final Check:")
    if Alice_key.key == Bob_key.key:
        print(" works")
    else:
        print(" something went wrong")  # reaching here means you've messed up the process somehow
