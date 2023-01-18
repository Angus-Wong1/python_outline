'''
Lesson Title: "Mastering Integers in Python"

Objective: By the end of this lesson, students will be able to understand and effectively use integers in Python programming, including basic operations, type conversion, and built-in functions.

Materials Needed:

  A computer with Python installed
  
  A text editor or IDE (Integrated Development Environment)
  
  I recommend sublime text(https://www.sublimetext.com/)

Introduction:

  Integers are a basic data type in Python that represent whole numbers, both positive and negative.
  
  Integers in Python can be represented using the int data type.

Basic Operations:

  Python supports the standard mathematical operations for integers, such as addition (+), subtraction (-), multiplication (*), division (/), and modulo (%).
  
'''
 
a = 5
b = 2
print(a + b) # 7
print(a - b) # 3
print(a * b) # 10
print(a / b) # 2.5
print(a % b) # 1

# Python also supports shorthand operators such as +=, -=, *=, /=, and %=.
a = 5
b = 2
a += b # a = a + b
a -= b # a = a - b
a *= b # a = a * b
a /= b # a = a / b
a %= b # a = a % b

#Type Conversion:
#Python allows you to convert integers to other data types using built-in functions such as int(), float(), and str()

a = 5
print(float(a)) # 5.0
print(str(a)) # "5"
b = "10"
print(int(b)) # 10

#Built-in Functions:
#Python has several built-in functions for working with integers, such as abs() for getting the absolute value, divmod() for getting the quotient and remainder of a division, and pow() for raising a number to a power.

a = -5
print(abs(a)) # 5
b = 7
c = 3
print(divmod(b, c)) # (2, 1)
print(pow(b, c)) # 343

'''
Task:

  Create a program that prompts the user for two integers and performs basic mathematical operations on them
  
  Create a program that prompts the user for a floating-point number and converts it to an integer, then prints the result

Conclusion:

  Integers are a fundamental data type in Python and are widely used in various applications.
  
  Understanding the basic operations and built-in


'''

