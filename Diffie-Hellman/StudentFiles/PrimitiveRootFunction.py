from sympy import factorint  # a strong factoring algorithm
from sympy import totient  # to factor non-prime Modulos, φ(n)

# used to find the least Primitive Root of prime p. The specifics of this method are left to personal investigation
# https://math.stackexchange.com/questions/124408/finding-a-primitive-root-of-a-prime-number
# https://www.geeksforgeeks.org/primitive-root-of-a-prime-number-n-modulo-n/
def LeastPrimitiveRoot(p):
    phi = totient(p)
    testlist = factorint(phi)
    test_power = []
    for i in testlist:
        test_power.append(int(phi/i))

    for int_test in range(1, 1000):  # 1000 is a large, arbitrary value.
        flag = False  # resets the flag for each new attempt
        for power in test_power:
            mod_test = pow(int_test, power, mod=p)
            if mod_test == 1:  # if we ever get 1 from our mod-test then it's not a primitive root, so we flag it.
                flag = True
                break

        if flag == False:
            return int_test

    # if we get here, our primitive root wasn't within 1000, so we raise an error to showcase this.
    raise f"{p} doesn't have a primitive root within 1000 values"