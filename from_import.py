# from import can be used avoid typing full name 
# but it is genedrally discoverd
from sys import argv
from math import sqrt

if len(argv) > 1:
        print 'The Number entered through commandline is', argv[1]
        x = int(argv[1])
        print 'The square root of it is', sqrt(x) 
else:
    print 'A number should entered as commandline argument !, try again'        