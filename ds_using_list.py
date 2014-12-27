# This is a shopping list 
shoppingList = ['Apple', 'Orange', 'Mango', 'Banana']

print 'The items to buy are :'
for item in shoppingList:
	print item

print 'I have %s items to buy' % len(shoppingList)
print 'I have to buy rice'
shoppingList.append('Rice')
print 'The shoppingList is now', shoppingList

print 'I will sort it now'
shoppingList.sort()
print 'The shoppingList is now', shoppingList

print 'The first item i will buy is', shoppingList[0]
olditem = shoppingList[0]
del shoppingList[0]
print 'The shoppingList is now', shoppingList

	