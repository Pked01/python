import time as t 

def main():
	current_time = t.localtime()
	print(current_time)

	if current_time[0] == 2015:
		print 'the year is 2014'

if __name__ == '__main__':
    main()
    		