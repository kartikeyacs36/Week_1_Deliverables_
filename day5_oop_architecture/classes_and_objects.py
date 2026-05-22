#classes and objects examples
class Student:
        name = name
        age = age
    
student1 = Student("Kartikeya", 22)
print(student1.name)  # Output: Kartikeya
print(student1.age)   # Output: 22        
student2 = Student("Jabir", 22)
print(student2.name)  # Output: Jabir
print(student2.age)   # Output: 22


class Employee:
    def __init__(self , name , age, role, salary): #init constructor
        self.name = name
        self.age = age
        self.role = role
        self.salary = salary
    def greet(self): #methods in class
        print(f"Hello {self.name}, good to see you! Your role is {self.role} and your salary is {self.salary}.")

employee1 = Employee("Kartikeya", 22, "Intern", 7000)
employee1.greet()
