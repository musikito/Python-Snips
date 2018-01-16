'''bisection search is an algorithm used to split a search in half and discard the other half'''

high, low = 100, 0
'''this are the end-points, change then as needed'''

print('Please think of a number between {0} and {1}!'.format(low, high))
'''ask the user for a number btw the end-points'''
'''use format to make more clear the print statement'''

guessing = True
while guessing:
    guess = (low + high) // 2
    '''use // to divide by int'''
    '''also declared the guess variable inside the while loop we don't have to re-define it again'''
    print('Is your secret number {0}?'.format(guess))
    ans = input("Enter 'h' to indicate the guess is too high. "
                    "Enter 'l' to indicate the guess is too low. "
                    "Enter 'c' to indicate I guessed correctly.").lower()
    '''convert to lower case, to be uniform'''
    if ans == 'h' :
        high = guess
    elif ans == 'l' :
        low = guess
    elif ans == 'c':
        guessing = False
    else:
        print('Sorry, I did not understand your input.')
        ''' in case user use something other than h, l, c'''

print('Game over. Your secret number was {0}.'.format(guess))