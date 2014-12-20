# This program prints 3N+1 sequence in python
# If number even divide by 2 or multiply by 2 and add 1 till output is 1

input_number = int(input("Enter a number : "))

while input_number != 1:
    
    if input_number <= 0:
       input_number = int(input('try again :'))
    elif input_number % 2 == 0:
       input_number = input_number // 2
       print input_number
    else:
       input_number = 3 * input_number + 1
       print input_number

          