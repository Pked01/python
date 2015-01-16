poem = '''\
programming is fun
if you want to make it more fun :
	use python !
'''
f = open('poem.txt', 'w')
f.write(poem)	
f.close()

f = open('poem.txt')
while True:
	line = f.readline()
	if len(line) == 0:
		break
	print line	
f.close()