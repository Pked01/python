''This program checks whether a number 
is a palindrome or not'''

# get a number as input
number = int(input('enter a number :'))

copy_of_number = number
sum = 0

while copy_of_number > 0:
	last_digit = copy_of_number % 10
	sum += last_digit ** 3
	copy_of_number /= 10

if sum == number:
	print 'The number {} is a Amstrong number'.format(number)
else:
    print 'The number {} is not a Amstrong number'.format(number)
    	
