# while loops can have else clause which is executed always 
# unless you break out 

number = 23
running = True

while running:
    
    guess = int(raw_input("Guess a number : "))

    if guess == number:
        print 'Your guess is right the number was', number
        running = False 
    elif guess < number:
        print 'The number is higher than your guess !' 
    else:
        print 'The number is lower than your guess !'

    
else:
    print 'The loop is over' 

print 'Done !'           