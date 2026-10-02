class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Employee(Person):
    def __init__(self,name, age , emp_id , emp_salary):
        super().__init__(name,age)
        self.emp_id=emp_id
        self.emp_salary=emp_salary

class Manager(Employee):
    def __init__(self, name, age, emp_id, emp_salary, department, teamsize):
        super().__init__(name, age, emp_id, emp_salary)
        self.department = department
        self.teamsize = teamsize


e1 = Employee("Durgesh", 21, 9370741286, 14000)
m1 = Manager("Asha", 30, 90809809, 90800, "justice", 10)

print(e1.name)
print(m1.emp_id)
print(m1.department)