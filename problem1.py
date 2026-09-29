class Student:#Created class
    def __init__(self,name,age,course): # init is a constructor which called itself as soon as object created , self tells the init which object you are working with
        self.name=name 
        self.age=age
        self.course=course
s1=Student("Durgesh",21,"AIML") # here we created object s1 , in student class we do pass parameter
s2=Student("Rahul",20,"CSE")
s3=Student("Course",22,"IT")

print(s1.name, s1.age, s1.course) # here we have to mention specific object.parameter if we want to see or there is another method display()
print(s2.name, s2.age, s2.course)
print(s3.name, s3.age, s3.course)