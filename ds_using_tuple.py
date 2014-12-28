# brackets are optional in tubles but is recommended
old_zoo = ('Lion', 'Tiger', 'Elephant')
print 'There are %d animals in the zoo' % len(old_zoo)
print 'They are', old_zoo
new_zoo = 'Python', old_zoo
print 'The animals in the new zoo are', new_zoo
print 'The animal is', new_zoo[0]
print 'The animals which came from the old zoo are', new_zoo[1]
print 'The last animal which came from the old zoo is', new_zoo[1][2]
