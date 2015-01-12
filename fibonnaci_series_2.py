n = int(input('Enter the range of the fibonacci series to be printed : '))

def fib(n):
    
    # create list to hold the numbers of the series
    numbers = [0] * (n + 1)
    numbers[1] = 1

    for i in range(2, n + 1):
          numbers[i] = numbers[i - 1] + numbers[i - 2]
    return numbers
    
print fib(n)          
