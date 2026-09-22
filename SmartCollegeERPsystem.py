class Person:
    college_name="GIT"
    university_name="Mumbai"
    academic_year="2026"
    def __init__(self,name,age,email="right",phone="231"):
        self.name=name
        self.age=age
        self.__email="Email098@gmail.com" 
        self.__phone="9970161286"
    def display(self):
        return f"Name: {self.name}\nAge: {self.age}\nEmail: {self.__email}\nphone: {self.__phone}"
    def emails(self,email):
        self.__email=email
    def set_email(self,email1):
        self.__email=email1
    def get_email(self):
        return f"Email:{self.__email}"
    def phones(self,phone="9970161286"):
        self.__phone=phone
    def set_phone(self,phone1):
        self.__phone=phone1
    def get_phone(self):
        return f"Phone number:{self.__phone}"
    def email_and_phone(self):
        choice=int(input("\n1.Email\n2.Phone\nEnter number of choice: "))
        while True:
            if choice==1:
                choice1=int(input("\n1.Set email\n2.See email\nEnter number of choice: "))
                while True:
                    if choice1==1:
                        self.set_email(input("Enter Email: "))
                        print("Email changed successfully")
                        break
                    elif choice1==2:
                        print(self.get_email())
                        break
                    else:
                        print("enter valid choice!!")
                        break
            elif choice==2:
                choice2=int(input("\n1.Set phone number\n2.See phone number\nEnter number of choice: "))
                while True:
                    if choice2==1:
                        self.set_phone(input("Enter phone number: "))
                        print("number changed successfully")
                        break
                    elif choice2==2:
                        print(self.get_phone())
                        break
                    else:
                        print("enter valid choice!!")
                        break
            else:
                print("Enter valid choice")
                break
                     
class Student(Person):
    def __init__(self, name, age, phone, email,roll_no,Department,semester):
        super().__init__(name, age, phone, email)
        self.roll_no=roll_no 
        self.Department=Department 
        self.semester=semester 
        self.__cgpa=8.1
        self.__fees_paid=1000
    def pay_fees(self,fees):
        if 1<=fees<=2000:
            self.__fees_paid+=fees
            return f"Fees Paid Successfully\n"
        else:
            f"We don't accept more or less\n"
    def update_cgpa(self,mark):
        self.__cgpa+=mark
        if self.__cgpa>10:
            return f"Please enter valid number\n"
        else:
            return f"Updated Cgpa: {self.__cgpa}\n"
    def view_result(self):
        return (super().display())+ f"\nRoll no. {self.roll_no}\nDepartment: {self.Department}\nSemester: {self.semester}\nCGPA: {self.__cgpa}"

class Teacher(Person):
    def __init__(self, name, age, phone, email,subject,salary,exp):
        super().__init__(name, age, phone, email)
        self.subject=subject
        self.salary=salary
        self.exp=exp

class Staff(Person):
    def __init__(self, name, age, phone, email,designation,shift):
        super().__init__(name, age, phone, email)
        self.designation=designation
        self.shift=shift

class GraduateStudent(Student):
    def __init__(self, name, age, phone, email, roll_no, Department, semester, cgpa,research_topic,guide_name):
        super().__init__(name, age, phone, email, roll_no, Department, semester, cgpa)
        self.research_topic=research_topic
        self.guide_name=guide_name
    def display(self):
        return (super().display()+f" he/she done research in this topic{self.research_topic} & his/her guide were {self.guide_name}")

class Admin:
    def __init__(self,password3):
        self.__password=password3    
    def change_password(self):
        password1=input("Enter new password (Press only Enter if you want to skip): ")
        if password1=="":
            print("Password remain unchaged")
        else:
            self.__password=password1  
    def get_password(self):
        return self.__password
    def login(self):
        while True:
            password = input("Enter password: ")
            if password == self.__password:
                self.change_password()
                return f"Password changed to {self.get_password()}\n"
            else:
                print("Password wrong, try again")
    
# a1=Admin("1234")
# print(a1.login(input("Enter password: "))) 
# p1=Person("Durgesh",21)      
# print(p1.email_and_phone()) 
# g1=Student("Durgesh",21,997161286,"Durgeshpadwal729@gmail.com",48,"AIML",8)   
# print(g1.pay_fees(input("Pay fees: ")),g1.update_cgpa(input("Update the cpga: ")),g1.view_result())

print(Person.college_name)

# graduate_student=GraduateStudent("Durgesh",21,9970161286,"abc098@gmail.com","54","AIML",7,7,"project","oak")
# user_name=input("Enter student details:\n Name:")
# user_age=input("\nEnter student age: ")
# user_phone=input("\nEnter phone number: ")
# user_email=input("\nEnter Email: ")
# user_Department=input("\nEnter Department: ")
# user_roll_no=input("\nEnter roll nunmber: ")
# user_semester=input("\nEnter user Semester: ")
# user_cgpa=input("\nEnter Cgpa: ")
# user_research_topic=input("\nEnter research topic: ")
# user_guide=input("\nEnter Guide name: ")
# l1=[user_name,user_age,user_phone,user_email,user_roll_no,user_Department,user_semester,user_cgpa,user_research_topic,user_guide]
# graduate_student1=GraduateStudent(*l1)
# print(graduate_student1.display(),"\n\n",graduate_student1.display())