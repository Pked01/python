# example of set in python
bri = set(['brasil', 'russia', 'india'])
print 'bri :', bri
print "'india' in bri :", 'india' in bri
print "'us' in bri :", 'us' in bri
bric = bri.copy()
print 'bri to bric :', bric
bric.add('china')
print 'add china to bric :', bric
print 'bric is superset of bri :', bric.issuperset(bri)
bric.remove('russia')
print 'remove russia from bric', bric
print 'bri & bric or bri.intersection(bric) condition returns :', bri & bric