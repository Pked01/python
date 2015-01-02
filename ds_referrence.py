print 'Simple Assingment'
shoplist = ['Apple', 'Mango', 'Orange', 'PineApple', 'Banana']
# copy reference to new variable
mylist = shoplist
del shoplist[0]
print 'shoplist :', shoplist
print 'mylist :', mylist

# copy using full slice
mylist = shoplist[:]

del mylist[0]

print 'shoplist :', shoplist
print 'mylist :', mylist