count = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
fruits = ['Apple', 'Orange', 'Mango', 'Pineapple', 'Banana']
change = [1, 'pennies', 2, 'dimes', 3, 'quaters']

for number in count:
	print 'This iscount %d' % number

for fruit in fruits:
	print 'This is a %s' % fruit

for i in change:
    print 'I got %r' % i

elements = []

for i in range(0,6):
    print 'Adding %d to elements' % i
    elements.append(i)

for i in elements:
    print 'The Element was %d' % i 
           	