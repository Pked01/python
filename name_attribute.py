# The name attribute can be used to find if a module 
# is run by itself or by any other module
def module_running():
    if __name__ == '__main__':
	        print 'This program is run by itself'
    else:
            print 'This program is imported by another module'	