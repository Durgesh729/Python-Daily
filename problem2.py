class Student:
    def __init__(self,name,age,sub):
        self.name=name 
        self.age=age
        self.sub=sub
    def display(self): # here we use display name function where self is use as parameter whenever user call this function like object.display() then parameter pass from that object will be display as how much we take in this function
        print(self.name, self.age, self.sub)
        
s1=Student("Durgesh",21,"AIML") 
s2=Student("Rahul",20,"CSE")
s3=Student("tej",22,"IT")

class Teacher:
    def __init__(self,name,course,classroom):
        self.name=name
        self.course=course
        self.classroom=classroom
    def display(self):
        print(self.name,self.course,self.classroom)

t1=Teacher("oak","oop",2)
t2=Teacher("Kolge","MP",3)
t3=Teacher("shinge","AI",1)

class Course:
    def __init__(self,name,Dept):
        self.name=name
        self.Dept=Dept
    def display(self):
        print(self.name,self.Dept)


c1=Course("AI","AIML")
c2=Course("MP","AIML")

#instead of this print statements 

# print(s1.name, s1.age, s1.sub)
# print(s2.name, s2.age, s2.sub)
# print(s3.name, s3.age, s3.sub)

# print(t1.name,t1.course,t1.classroom)
# print(t2.name,t2.course,t2.classroom)
# print(t3.name,t3.course,t3.classroom)

# print(c1.name,c1.Dept)
# print(c2.name,c2.Dept)

# we use this method

s1.display()
s2.display()
s3.display()
t1.display()
t2.display()
t3.display()
c1.display()
c2.display()