class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eat(self):
        return f"{self.name} is eating"
    def sleep(self):
        return f"{self.name} is sleeping"

class Dog(Animal):
    def __init__(self,name,age,breed):
        super().__init__(name,age)
        self.breed=breed
    def bark(self):
        return f"{self.name} is barking"
    def display(self):
        return f"name:{self.name} age:{self.age} breed:{self.breed}"

a1=Animal("Monkey",10)
d1=Dog("cow",14,"yes")

print("Animal object:", a1.name, a1.age)
print("Dog object:", d1.name, d1.age)
print("Dog inherits Animal:", issubclass(Dog, Animal))
print(d1.name)
print(d1.breed())