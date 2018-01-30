def F(n):
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    elif (n > 1):
        return (F(n-1) + F(n-2))
    else:
        return -1