n = int(input('Enter a number to check if its a palindrome : '))

def check_palin(n):
    if str(n) == str(n)[::-1]:
            print 'The number %d is a Palindrome !' % n
    else:
            print 'The number %d is not a Palindrome' % n

check_palin(n)                    