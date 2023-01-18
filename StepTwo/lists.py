# Lesson: Python Lists

# Introduction:
# In Python, a list is a collection of items that are ordered and changeable. Lists are written with square brackets [] and items are separated by commas.

# Creating a List:
# You can create a list by placing items inside square brackets and separating them with commas. For example:
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]

# Accessing Items in a List:
# You can access items in a list by referring to their index number. Index numbers start at 0, not 1. For example:
print(fruits[0]) # Output: "apple"
print(numbers[2]) # Output: 3

# Modifying Items in a List:
# You can change an item in a list by referring to its index number and assigning a new value to it. For example:
fruits[0] = "orange"
print(fruits) # Output: ["orange", "banana", "cherry"]

# Adding Items to a List:
# You can add an item to a list by using the "append()" method or the "+" operator. For example:
fruits.append("mango")
print(fruits) # Output: ["orange", "banana", "cherry", "mango"]

vegetables = ["carrot", "potato"]
grocery_list = fruits + vegetables
print(grocery_list) # Output: ["orange", "banana", "cherry", "mango", "carrot", "potato"]

# Removing Items from a List:
# You can remove an item from a list by using the "remove()" method or the "del" keyword. For example:
fruits.remove("orange")
print(fruits) # Output: ["banana", "cherry", "mango"]

del fruits[1]
print(fruits) # Output: ["banana", "mango"]

# Other List Methods:
# - len(list): Returns the number of items in a list
# - list.count(item): Returns the number of times an item appears in a list
# - list.sort(): Sorts the items in a list in ascending order
# - list.reverse(): Reverses the order of the items in a list

# Example:
print(len(fruits)) # Output: 2
print(fruits.count("banana")) # Output: 1
fruits.sort()
print(fruits) # Output: ["banana", "mango"]
fruits.reverse()
print(fruits) # Output: ["mango", "banana"]

# Conclusion:
# Lists are an important and useful data structure in Python. They allow you to store, access, and modify a collection of items in a specific order. With the methods and techniques covered in this lesson, you should now have a good understanding of how to work with lists in Python.
