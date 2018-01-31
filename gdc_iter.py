#The greatest common divisor of two positive integers is the largest integer that divides each of them without remainder. For example,
#gcd(2, 12) = 2
#gcd(6, 12) = 6
#gcd(9, 12) = 3
#gcd(17, 12) = 1

def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''

    testVal = 1

    if a % b == 0:
        return b

    for k in range(int(b / 2), 0, -1):
        if a % k == 0 and b % k == 0:
            testval = k
            break
    return testval

print (gcdIter(12,2))