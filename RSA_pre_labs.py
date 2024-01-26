def sign(a): #Python doesn't have sign primitively, and I don't want to import math here because that includes a gcd implementation
    if (a > 0): return 1
    elif (a == 0): return 0
    elif (a < 0): return -1
    else: return float('nan')

def gcd(a, b): #Performs the given algorithm; I know there's a cleaner way to do this from outside knowledge, though
    remainders = [a, b]
    if (abs(b) > abs(a)): remainders = [b, a]
    quotients = []
    while (remainders[-1] != 0):
        quotients.append(remainders[-2] // remainders[-1])
        remainders.append(remainders[-2] - quotients[-1] * remainders[-1])
    return abs(remainders[-2])

#Here's the implementation I came up with based on the EEA question
#(find x and y such that ax + by = gcd(a, b)) before reading your algorithm
def eea1(a, b):
    g = gcd(a, b)
    if (g == 0): return (0, 0)
    x = 0
    y = 0
    x_step = a // g
    y_step = b // g
    while True:
        if (x * x_step - y * y_step == 1): return (x, -y)
        elif (y * y_step - x * x_step == 1): return (-x, y)
        elif (x * x_step > y * y_step): y += sign(b)
        else: x += sign(a)

def eea2(a, b): #Full EEA
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

def ordString(str): #Converts a string to an integer. Integers are unbounded in Python, so no need to worry about overflow.
    num = 0
    for i in range(len(str)):
        num += ord(str[i]) * 256**i
    return num

def chrString(num): #Converts an integer to a string. 
    str = ""
    if (num == 0): return chr(0)
    charnum = 0
    while (num > 0):
        charnum = num % 256
        str += chr(charnum)
        num //= 256
    return str

#Testing
print(gcd(527, 341))
v1 = 999
v2 = 51
e = eea2(v1, v2)
print(e)
print((e[1] * v1 + e[2] * v2) // e[0]) #Should return 1 no matter what v1 and v2 are (unless both are zero, in which case this doesn't work)
print(ordString("Here is a string for you."))
print(chrString(ordString("Here is a string for you.")))