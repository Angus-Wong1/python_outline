# question one
'''
class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("The car is driving")

car1 = Car("Toyota", "Camry", 2020, "Blue")
car1.drive()

'''

# question two
'''
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def greet(self):
        print(f"Hello, my name is {self.name}")

person1 = Person("John", 30, "123 Main St")
person1.greet()
'''
#question three
'''
class BankAccount:
    def __init__(self, account_number, balance, owner_name):
        self.account_number = account_number
        self.balance = balance
        self.owner_name = owner_name

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def check_balance(self):
        return self.balance

account1 = BankAccount("12345", 1000, "John")
account1.deposit(500)
print(account1.check_balance()) # 1500
account1.withdraw(300)
print(account1.check_balance()) # 1200
'''

#question four 

'''
class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}\nEmployee ID: {self.employee_id}\nSalary: {self.salary}")

class Manager(Employee):
    def __init__(self, name, employee_id, salary, department):
        super().__init__(name, employee_id, salary)
        self.department = department

    def assign_task

'''

#question five
'''
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

circle1 = Circle(5)
print(circle1.calculate_area())

rectangle1 = Rectangle(10, 20)
print(rectangle1.calculate_area())

triangle1 = Triangle(5, 10)
print(triangle1.calculate_area())
'''
