def print_factors(x):
	'''This function prints all the factors 
	of a number given as argument to i'''

	
	for i in range(1, x + 1):
		try :
		    if x % i == 0:	
			    print(i)
		except ZeroDivsionError:
		    print 'The number should be positive, try again !'


num = int(input('Enter a number : '))
print_factors(num)