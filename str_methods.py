name = 'K.Parthibhan'
# Check it starts with 'K.p'
if name.startswith('K.P'):
	print 'The name be called in short as K.P'

# use 'in' operator to check if  letter 'a' is present
if 'a' in name:
    print 'letter \'a\' is present in the name'

# find() method returns -1 if given string
# is not a substring of a string.
if name.find('Parthi') != -1:
    print 'Yes, it contains \'Parthi\''

# join() method is used to join a sequence with delimiter
delimiter = '__*__' 
mylist = ['India', 'Australia', 'South Africa', 'New Zealand'] 
print delimiter.join(mylist) 
delimiter = '......'	
newlist = ['1,2,3', 'N']
print delimiter.join(newlist)