class Robot:
    
    # class variable
    population =  0

    def __init__(self, name):
        
        # Object variable       
        self.name = name
        print "(Initializing {} )".format(self.name)
        Robot.population += 1

    def die(self):
         
         print '{} is being destroyed'.format(self.name)
         Robot.population -= 1
         if Robot.population == 0:
             print '{} was the last Robot'.format(self.name)
         else:
             print 'There are still {} robots at work'.format(Robot.population)

    def say_hi(self):
        
        print 'Greetings from {}'.format(self.name)

    @classmethod
    def how_many(cls):
        print 'We have {} robots'.format(cls.population)

robot1 = Robot("R1-D1")
robot1.say_hi()
Robot.how_many()

robot2 = Robot("R2-D2")
robot2.say_hi()
Robot.how_many()

robot1.die()
Robot.how_many()
robot2.die()
Robot.how_many()
