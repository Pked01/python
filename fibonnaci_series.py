# fibonnaci series using looping technique
def fib(n):
    a,b = 1,1
    for i in range(n-1):
         a,b = b, a+b
    return a

n = int(input('Enter a number'))
print 'The fibonnaci series is'
print fib(n)