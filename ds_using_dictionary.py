address_book = { 'Parthibhan' : 'parthibhank82@gmail.com',
                 'promotions' : 'promos@promail.com',
                 'Steve Jobs' : 'steve@apple.com',
                 'Spammer'    : 'spammer@spammail.com'
               }
               
print 'Contact me at', address_book['Parthibhan'] 

del address_book['Spammer']
print 'The are {} contacts present '.format(len(address_book))

for name, address in address_book.items():
      print 'Contact {} at {}'.format(name, address) 

address_book['Guido'] = 'guido@python.org'
print '\nGuido\'s address is', address_book['Guido']


