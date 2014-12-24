# values of parameter can be given using names instead of positions
def func(a=2, b=4, c=23):
	print 'a is ', a, 'b is', b, 'c is', c

func(3,4)
# specify arguments using keywords(names)
func(b=25, c=45)
func(3, c=23)
func(c=56, a=94)