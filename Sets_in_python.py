# example of set in python
bri = set(['brasil', 'russia', 'india'])
print 'india' in bri
print 'us' in bri
bric = bri.copy()
print 'bric', bric
bric.add('china')
print 'bric', bric
print 'bric is superset of bri', bric.issuperset(bri)
bric.remove('russia')
print 'bric', bric
print 'bri & bric or bri.intersection(bric)', bri & bric