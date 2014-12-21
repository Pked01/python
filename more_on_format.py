# decimel(.) precision of three for 0.3333
print '{0:.3f}'.format(1.0/3)
# decimel(.) precision of 7 
print '{0:.7f}'.format(1.0/3)
# decimel precision 5 
print '{0:.5f}'.format(55.0/33)
# fill with underscores if width is less
print '{0:_^5}'.format('Hello')
print '{0:_^6}'.format('Hello')
print '{0:_^11}'.format('Hello')
print '{0:_^1000}'.format('Hello')
# keyword-based
print '{name} wrote this {program} code'.format(name = 'parthibhan', program = 'python')
# prevent line feed being printed usin comma
print 'a',
x = 'a'
print x,
print 'a with line feed'
print 'a'