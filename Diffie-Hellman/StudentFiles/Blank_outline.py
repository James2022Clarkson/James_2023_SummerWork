from PrimitiveRootFunction import LeastPrimitiveRoot
# useful for finding a Primitive Root of a value


# Diffie-Hellman Class can be created in a different file and imported, or here.
class DH:
    def __init__(self, prime, primative_root):
        """any initial processes should occur here"""
        self.prime, self.primative_root = prime, primative_root

    def Exchangeable_generation(self, secret_value):
        """create the half-key that can be exchanged with the other side here"""
        return exchangeable

    def Final_key_generation(self, half_key, secret_value):
        """using the same secret_value from Exchangeable_generation, finish the key received from another instance"""
        return secret_key


if __name__ == '__main__':
    # Demonstrate the process of using your class here.
    # The only data exchanged between the two generated class instances should be the half-keys and initial values.



    # the end resulting check should be similar to this:
    if Alice_key == Bob_key:
        print("keys are identical")
    else:
        print("keys are different, you've messed up!")
