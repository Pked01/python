# default values for function parameter given using assignment operator
# default parameter should be last parameter and be immutable
def say(message, times=1):
	print message * times

# print the string once
say('Hello')
# print string five times
say('Hello', 5)