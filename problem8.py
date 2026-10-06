class Employee:
    company_name="WisdomSprouts PVT LTD"
    def __init__(self,employee_id,name,salary):
        self.employee_id=employee_id
        self.name=name
        self.salary=salary
    def display(self):
        return f"{self.employee_id}|{self.name}:salary: {self.salary} "
s1=Employee(1,"Durgesh",9000)
s2=Employee(2,"Aditya",7800)
s3=Employee(3,"Kishor",0.001)
print(s1.company_name,"\n",s1.display(),"\n",s2.display(),"\n",s3.display())
    