#this is a small fizz-buzz sort/program
#usually is to write a program or snipet that prints the numbers from 1 to n
#but for multiples of x print 'Fizz' an for multiple of y print Buzz
#here we use if, elif, else
for num in range(1, 21):
    '''we will use the # 1 to 20, and be multiples of 3 and 5'''
    if num % 3 == 0 and num % 5 == 0:
        '''we use modulo to verify that indeed is multiplo of x and y'''
        print('FizzBuzz')
    elif num % 3 == 0:
        '''if num is modulo of x(in this case 3), then is multiplo of x and we print Fizz'''
        print('Fizz')
    elif num % 5 == 0:
        '''instead is multiplo of y(in this case 5), then we print Buzz'''
        print('Buzz')
    else:
        '''if is neither then just print the number'''
        print(num)