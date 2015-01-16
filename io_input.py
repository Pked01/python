def reverse(text):
	return text[::-1]

def is_palindrome(text):
    return text == reverse(text)

something = raw_input("Enter text : ")

if is_palindrome(something):
	print 'Yes, it is a plaindrome'
else:
    print 'No, it is not a plaindrome'
    	