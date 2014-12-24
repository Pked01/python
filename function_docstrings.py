# This program is an example of DocStrings
def print_max(x, y):
    '''Prints the largest of the two arguments.

    The two values must be integers.'''

    # convert to integers, if possible
    x = int(x)
    y = int(y)

    if x > y:
        print x, 'is maximum'
    elif y > x:
        print y, 'is maximum'
    else:
        return

print_max(5,7)
print print_max.__doc__                