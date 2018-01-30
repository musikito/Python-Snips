#more elegant form of Fibonacci numbres recursively
def GenerateFibonaci(x):

    if(x == 0):
        return 0

    elif(x == 1):
        return 1

    else:
        return GenerateFibonaci(x-1) + GenerateFibonaci(x-2)

#main

x = int(input("Enter the term till which you wnat to generate fibonacci sequence: "))

for i in range(x):
    print(GenerateFibonaci(i))