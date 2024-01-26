import math
import random

#Imported from pre-lab

#Extended Euclidean Algorithm: returns (g, x, y) such that x * a + b * y = g = GCD(a, b)
def eea(a, b):
    remainders = [a, b]
    if (abs(b) > abs(a)): remainders = [b, a]
    quotients = []
    bezout1 = [1, 0]
    bezout2 = [0, 1]
    while (remainders[-1] != 0):
        quotients.append(remainders[-2] // remainders[-1])
        bezout1.append(bezout1[-2] - quotients[-1] * bezout1[-1])
        bezout2.append(bezout2[-2] - quotients[-1] * bezout2[-1])
        remainders.append(remainders[-2] - quotients[-1] * remainders[-1])
    if (abs(b) > abs(a)): return (abs(remainders[-2]), bezout2[-2], bezout1[-2])
    else: return (abs(remainders[-2]), bezout1[-2], bezout2[-2])

#Converts a string to an integer. Integers are unbounded in Python, so no need to worry about overflow.
def ordString(str):
    num = 0
    for i in range(len(str)):
        num += ord(str[i]) * 256**i
    return num

#Converts an integer to a string.
def chrString(num): 
    str = ""
    if (num == 0): return chr(0)
    charnum = 0
    while (num > 0):
        charnum = num % 256
        str += chr(charnum)
        num //= 256
    return str

#New stuff

primes = [2] #A global list of primes

#Updates primes to contain all of the primes up to (and including) max; I already knew this algorithm from elsewhere, and I implemented it here for the sake of key generation
def primesUpdate(max):
    global primes
    while (max > primes[-1]**2): primesUpdate(primes[-1]**2 - 1)
    sieveList = []
    for i in range(2, max + 1): sieveList.append(True)
    for p in primes:
        i = p * 2 - 2
        while (i < len(sieveList)):
            sieveList[i] = False
            i += p
    primes = []
    for i in range(0, len(sieveList)):
        if sieveList[i]: primes.append(i + 2)

#Divides a by gcd(a, b) until gcd(a, b) is 1, to ensure a is coprime to b, then returns the new a
def makeCoprime(a, b):
    if (a == 0): return 0
    if (b == 0): return a
    while(math.gcd(a, b) != 1): a //= math.gcd(a, b)
    return a

class RSA:
    
    #Returns a pair of pairs: the first pair is the public key, the second pair is the private key.
    #numSize is the integer we want to encrypt; this method doesn't do the encryption, but we need to know the size of the number so we can choose appropriately-sized primes
    def getKeys(numSize):
        primesUpdate(math.isqrt(numSize) * 5) #The * 5 is arbitrary; we just want to make sure that the primes chosen multiply to a number larger (but not too much larger, to save time on prime calculations) than numSize
        p = random.choice(primes)
        q = random.choice(primes)
        while p == q: q = random.choice(primes) #This is just to make sure that p and q are different primes
        while (p * q < numSize):
            p = random.choice(primes)
            q = random.choice(primes)
            while p == q: q = random.choice(primes)
        n = p * q
        totient = (p - 1) * (q - 1)
        e = random.randrange(1, totient)
        e = makeCoprime(e, totient)
        d = pow(e, -1, totient)
        return ((e, n), (d, n))

    def encrypt(message, key): return pow(message, key[0], key[1])
    def decrypt(message, key): return pow(message, key[0], key[1]) #These two do the same thing, but the user of the class doesn't need to know that

#Testing
istr = 1000000000  
keys = RSA.getKeys(istr)       
print(keys)
print(istr % keys[0][1])
encrypted = RSA.encrypt(istr, keys[0])
print(encrypted)
decrypted = RSA.decrypt(encrypted, keys[1])
print(decrypted)