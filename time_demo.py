import time

t0 = time.clock()

while(True):
    print 'Hello'
    if((time.clock() - t0) > 4):
    	print 't0 : ', t0
    	print 't1 : ', time.clock()
    	print 't1 - t0', time.clock() - t0
        break

