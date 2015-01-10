# fibonnaci series using looping technique
range = int(input('Enter length of the fibonnaci series to be printed : '))

if range < 2:
	n = int(input('Enter a number greater than 2 : '))

a, b = 0, 1
count  = 2
print 'Printing first %d numbers in the fibonnaci series.................' % range
print a

while count < range + 1:
    print b
    a, b = b, a+b
    count += 1
	
