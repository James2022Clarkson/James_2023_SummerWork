from sympy import factorint  # a strong factoring algorithm
from sympy import totient  # to factor non-prime Modulos, φ(n)


# This file contains several Primitive Root based functions(calculating, verifying, showcasing)
# Primitive roots are useful for Diffie-Hellman, and that is the point of this file, along with demonstrations.
# running this file will showcase the various functions: see line 79


# used to find the least Primitive Root of prime p. The specifics of this method are left to personal investigation
# https://math.stackexchange.com/questions/124408/finding-a-primitive-root-of-a-prime-number
# https://www.geeksforgeeks.org/primitive-root-of-a-prime-number-n-modulo-n/
def LeastPrimitiveRoot(p, prints):
    phi = totient(p)
    testlist = factorint(phi)
    test_power = []
    for i in testlist:
        test_power.append(int(phi/i))

    for int_test in range(1, 1000):  # 1000 is a large, arbitrary value.
        if prints:
            print("testing:", int_test)
        flag = False  # resets the flag for each new attempt
        for power in test_power:
            mod_test = pow(int_test, power, mod=p)
            if prints:
                print(f"{int_test}^{power} mod {p} =", mod_test)
            if mod_test == 1:  # if we ever get 1 from our mod-test then it's not a primitive root, so we flag it.
                if prints:
                    print(f"{int_test} resulted in a 1, and thus will not work")
                flag = True
                break

        if flag == False:
            return int_test

    # if we get here, our primitive root wasn't within 1000, so we raise an error to showcase this.
    raise f"{p} doesn't have a primitive root within 1000 values"


# a simple demonstration of a possible Primitive Root test.
def primitive_root_test(root, modulo):
    """Does not calculate, merely tests Primitive Root. Will not work if root = modulo
    returns True/False"""
    return printable_primitive_root_test(root, modulo, False)

def printable_primitive_root_test(root, modulo, prints):
    """Does not calculate, merely tests. Will not work if root = modulo
    returns visualization/steps of results if prints = True"""
    num_of_results = totient(modulo)
    for i in range(1, modulo+1):
        loopval = pow(root, i, modulo)
        if prints: print(f"{root}^{i} mod {modulo} =", loopval)
        if loopval == root and i > 1:
            break

    if prints:
        print(f"root {root} of mod {modulo} goes through {i - 1} values compared to the possible {num_of_results}")
    return i-1 == num_of_results



def Primative_demo(g, c):
    """ assumes 'g' is 'c's Primitive Root\n
    if 'g' is not a Primitive Root the function will not display the correct final answer"""
    loopsize = int(totient(c))  # totient in its raw return is not usable with the pow() function
    for i in range(loopsize+2):
        value = pow(g, i, c)
        print(f"{g} ^ {i} mod {c} = {value}")
    print("\nthis then loops, since...")
    print(f"    {g} ^ {loopsize} mod {c} = {pow(g, loopsize, c)}")
    print(f"This means that, since we know...")
    print(f"    {g} ^ {i} mod {c} = ({g} ^ {loopsize}) * ({g} ^ 1) mod {c}")
    print(f"    and since {g} ^ {loopsize} mod {c} = 1...")
    print(f"    {g} ^ {i} mod {c} = 1 * ({g} ^ 1) mod {c} = {value}")
    print(f"We're then back to the original values, to continue looping\n")


if __name__ == '__main__':
    # examples of functions in action:
    Primative_demo(3, 7)

    printable_primitive_root_test(3, 7, prints=True)

    print(LeastPrimitiveRoot(7, prints=True))
