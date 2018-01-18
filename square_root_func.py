#a function definition that accepts a value n
#  and returns the square root of n after making 20 guesses.
def squareroot(n):
    root = n/2    #initial guess will be 1/2 of n
    for k in range(20):
        root = (1/2)*(root + (n / root))

    return root

print (squareroot(9))