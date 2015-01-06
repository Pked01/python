# init methods are used to do initialization 
# while creating a new instance
class Person:
	def __init__(self, name):
		self.name = name   # name is a local variable

	def say_hi(self):
	    print 'Hi, my name is', self.name  # self.name is the field of an Object

p = Person('Parthibhan')
p.say_hi()	    	