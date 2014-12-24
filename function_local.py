x = 50

def func(x):
	print 'x is',x
	# local assingment, here x is local to the function
	x = 3
	print 'x is changed to',x

func(x)	

# The value change doesnot affect x in main block
print 'x is still' ,x
	