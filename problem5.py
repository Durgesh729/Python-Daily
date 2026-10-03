class Student:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
class Sports(Student):
    def __init__(self,name,roll_no):
        super().__init__(name,roll_no)
    def play(self):
        print(f"{self.name} is playing")
    def practice(self):
        print(f"{self.roll_no} is practicing")
class Academics(Student):
    def __init__(self,name,roll_no):
        super().__init__(name,roll_no)
    def study(self):
        print(f"{self.name} is studying")
    def exam(self):
        print(f"{self.roll_no} is in exam")

s1=Sports("Durgesh",54)
a1=Academics("tej",14)
