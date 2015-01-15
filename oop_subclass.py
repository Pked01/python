class SchoolMember:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print '(Initialized SchoolMember : {})'.format(self.name)

    def tell(self):
        print 'Name : {}, Age : {}'.format(self.name, self.age)

class Teacher(SchoolMember):

    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print '(Initialized Teacher: {})'.format(self.name)

    def tell(self):
        SchoolMember.tell(self)
        print 'Salary: "{}"'.format(self.salary)

class Student(SchoolMember):
    
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print '(Initialized Student: {})'.format(self.marks)                       

    def tell(self):
        SchoolMember.tell(self)
        print 'marks: {}'.format(self.marks)    

t = Teacher('Mr. Rasarasan', 55, 12000)
s = Student('K.parthibhan', 17, 175)

print 

members = [t, s]

for member in members:
   member.tell() 