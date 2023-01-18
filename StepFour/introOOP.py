'''
Lesson Title: "Mastering Object-Oriented Programming in Python"

Objective: By the end of this lesson, students will be able to understand and effectively use object-oriented programming (OOP) concepts in Python, such as classes, objects, inheritance, and polymorphism.

Materials Needed:

  A computer with Python installed
  
  A text editor or IDE (Integrated Development Environment)
 
Introduction:

  Object-oriented programming (OOP) is a programming paradigm that uses the concept of objects, which have properties and methods, to represent and manipulate data.
  
  In Python, OOP is implemented through classes, which are templates for creating objects.

Classes and Objects:

  A class is a blueprint for creating objects, which are instances of the class.
  
  A class definition typically includes a constructor (init method), properties, and methods.
'''
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!")

dog1 = Dog("Fido", "Golden Retriever")
dog2 = Dog("Buddy", "Labrador Retriever")

print(dog1.name) # "Fido"
dog1.bark() # "Woof!"

'''
Homework Problems:

1. Create a class "Car" that has properties for make, model, year, and color. The class should also have a method "drive" that prints "The car is driving" when called. Create an instance of the class and set the properties to "Toyota", "Camry", 2020, "Blue" respectively. Then, call the drive method on the instance.

2. Create a class "Person" that has properties for name, age, and address. The class should also have a method "greet" that prints "Hello, my name is {name}" when called. Create an instance of the class and set the properties to "John", 30, "123 Main St" respectively. Then, call the greet method on the instance.

3. Create a class "BankAccount" that has properties for account number, balance, and owner name. The class should also have methods "deposit", "withdraw" and "check_balance" that can be used to deposit, withdraw and check the balance respectively. Create an instance of the class and set the properties to "12345", 1000, "John" respectively. Then, call the deposit, withdraw, and check_balance methods on the instance to check the balance after each transaction.

4. Create a class "Employee" that has properties for name, employee_id, and salary. The class should also have a method "display_info" that prints all the properties when called. Create a subclass "Manager" that inherits from the Employee class and has a property for department and a method "assign_task" that can be used to assign a task to an employee. Create instances of both classes and call the display_info and assign_task methods on the instances.

5. Create classes "Circle", "Rectangle", and "Triangle" that have properties for radius, width, height, and base respectively. Each class should have a method "calculate_area" that calculates and returns the area of the shape when called. Create instances of each class and call the calculate_area method on the instances.

See answers at introOOP_answers.py
'''
