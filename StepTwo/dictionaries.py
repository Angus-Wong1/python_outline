'''
Lesson: Indexing, Slicing, Adding, and Removing Elements in Python Dictionaries

In this lesson, we will learn about different ways of working with elements in Python dictionaries.

Indexing

In Python dictionaries, elements are accessed using their keys, instead of using an integer index like in lists. To access an element in a dictionary, we use the key inside square brackets [].
'''
# Accessing elements in a dictionary
my_dict = {"name": "John", "age": 30, "address": "123 Main St"}
print(my_dict["name"]) # Output: John

#It's also possible to use the get() method to access a value by its key. This method returns None #if the key is not found, instead of raising an error.
'''
Slicing

Dictionaries are unordered collections of key-value pairs, so slicing is not applicable. However, we can use the items() method which returns a view of the dictionary's items in the form of key-value pairs.
'''

# Using items() method
my_dict = {"name": "John", "age": 30, "address": "123 Main St"}
for key, value in my_dict.items():
    print(key, value)

#Adding

#To add a new key-value pair to a dictionary, we can simply assign a value to a new key.
# Adding elements to a dictionary
my_dict = {"name": "John", "age": 30, "address": "123 Main St"}
my_dict["gender"] = "male"
print(my_dict) # Output: {"name": "John", "age": 30, "address": "123 Main St", "gender": "male"}

'''
Removing

To remove an element from a dictionary, we can use the del keyword and specify the key of the element to be deleted.
'''
# Removing elements from a dictionary
my_dict = {"name": "John", "age": 30, "address": "123 Main St"}
del my_dict["age"]
print(my_dict) # Output: {"name": "John", "address": "123 Main St"}

# It's also possible to use the pop() method to remove an item and return its value. This method # raises an error if the key is not found.
# Removing elements from a dictionary using the pop() method
my_dict = {"name": "John", "age": 30, "address": "123 Main St"}
age = my_dict.pop("age")
print(my_dict) # Output: {"name": "John",
