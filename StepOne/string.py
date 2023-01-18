'''
Lesson Title: "Mastering Strings in Python"

Objective: By the end of this lesson, students will be able to understand and effectively use strings in Python programming, including basic operations, string methods, and string formatting.

Materials Needed:

A computer with Python installed
 
A text editor or IDE (Integrated Development Environment)

I recommend sublime text(https://www.sublimetext.com/)

Introduction:

  Strings are a basic data type in Python that represent sequences of characters.
  
  Strings in Python can be represented using the str data type and can be declared using single quotes ('...') or double quotes ("...").

Basic Operations:

Python supports the standard operations for strings, such as concatenation (+) and repetition (*).

'''
a = "Hello"
b = "world"
print(a + " " + b) # "Hello world"
print(a * 3) # "HelloHelloHello"

# Python also supports indexing and slicing of strings.
a = "Hello"
print(a[1]) # "e"
print(a[1:4]) # "ell"

#String Methods:
#Python has several built-in methods for working with strings, such as upper() for converting a string to uppercase, lower() for converting a string to lowercase, and strip() for removing leading and trailing whitespace.
a = "Hello"
print(a.upper()) # "HELLO"
print(a.lower()) # "hello"
b = "   Hello   "
print(b.strip()) # "Hello"
#Python also has several other useful string methods such as find() for finding the index of a substring, replace() for replacing a substring, and split() for splitting a string into a list of substrings.

#String Formatting:
#Python allows you to format strings using placeholders and the format() method.
name = "John"
age = 30
print("My name is {} and I am {} years old.".format(name, age)) # "My name is John and I am 30 years old."

'''
Task:

  Create a program that prompts the user for a string and performs basic operations on it
  
  Create a program that prompts the user for a string and uses string methods to manipulate it

'''



