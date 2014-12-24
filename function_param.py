# This takes two integer parameters prints their comparison
def print_comparision(a,b):
	if a > b:
		print a, 'is greater than' ,b
	elif b > a:
		print b, 'is greater than' ,a
	else: 
	    print a, 'is equal to' ,b

# directly pass literal values
print_comparision(3,5)

# pass variables as parameters
x = 2
y = 2

print_comparision(x,y)

x += 1

print_comparision(x,y)

y += 2
x -= 2

print_comparision(x,y)
