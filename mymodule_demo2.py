from mymodule import speak, __version__
from name_attribute import module_running

if __name__ == '__main__':
	print 'This is main module'

speak()
print 'Version', __version__

print 'name_attribute :', module_running()