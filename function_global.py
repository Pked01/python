# using global statement specify a variable is a global variable
x = 50

def func():
    global x
    print 'x is' ,x

    # change effects the varible x in the main block
    x = 2
    print 'x is changed to' ,x

func()

# the assignment is not local to the function
print 'x is now' ,x

