from sympy import factorint, nextprime

from random import randrange



def totient(n):

    if (n < 0): return totient(-n)

    if (n == 1): return 0

    factors = factorint(n)

    result = 1

    for p in factors: result *= (p**(factors[p] - 1) * (p - 1))

    return result



def primitiveRootsCheck(num, modulus):

    remainders = []

    for power in range(1, totient(modulus) + 1):

        checked = pow(num, power, modulus)

        if checked in remainders: return False

        remainders.append(checked)

    return True



def simulateDiffieHellman(pSize):

    modulus = nextprime(pSize)

    root = randrange(2, modulus)

    while not primitiveRootsCheck(root, modulus): root = randrange(2, modulus)

    a = randrange(2, modulus)

    b = randrange(2, modulus)

    A = pow(root, a, modulus)

    B = pow(root, b, modulus)

    key1 = pow(A, b, modulus)

    key2 = pow(B, a, modulus) #key1 and key2 should be equal

    print("Prime: " + str(modulus) + " Root: " + str(root) + " A: " + str(A) + " B: " + str(B))

    if (key1 == key2): return key1

    else: raise ArithmeticError("The keys were not equal, which means something is wrong with this code.")

    

#Testing

print(simulateDiffieHellman(randrange(10000)))

print(simulateDiffieHellman(randrange(10000)))

print(simulateDiffieHellman(randrange(10000)))

print(simulateDiffieHellman(randrange(10000)))

print(simulateDiffieHellman(randrange(10000)))

print(simulateDiffieHellman(randrange(100000)))

print(simulateDiffieHellman(randrange(100000)))

print(simulateDiffieHellman(randrange(100000)))

print(simulateDiffieHellman(randrange(100000)))

print(simulateDiffieHellman(randrange(100000)))



