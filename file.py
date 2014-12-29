from sys import argv
script, filename = argv
txt = open(filename)
print 'The file is', filename
print txt.read()

print 'another file:'
new_file = raw_input('>')
new_txt = open(new_file)
print new_txt.read()
