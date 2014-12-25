import sys

print 'The commang line aurguments are :'
for i in sys.argv:
	print i
print 'sys.argv[1] is', sys.argv[1]
print 'sys.argv[0] is', sys.argv[0], '(The name of the program !)'
print 'python starts counting from zero !'

print '\n\n PYTHONPATH IS :', sys.path, '\n'
	