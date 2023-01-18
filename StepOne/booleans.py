'''
Lesson: Booleans in Python

In this lesson, we will learn about booleans in Python, including what they are, how to create them, and how to use them in control structures.

What are Booleans?

In Python, a boolean is a data type that can have one of two values: True or False. These values are used to represent the truth or falsity of a statement. Booleans are often used in control flow statements, such as if and while loops, to determine whether a certain block of code should be executed or not.

Creating Booleans

A boolean can be created by assigning the value True or False to a variable.
'''

# Creating a boolean
is_python_fun = True
is_python_difficult = False

#We can also create booleans using comparison operators such as ==, !=, >, <, >=, and <=. These operators will return a boolean value based on the comparison.
# Comparing values
x = 5
y = 2
result = x > y
print(result) # True

'''
Boolean Operators

Python also has several boolean operators that can be used to combine multiple boolean values. These operators include and, or, and not.

The and operator returns True if both the operands are True, else it returns False.
The or operator returns True if either of the operands is True, else it returns False.
The not operator returns the opposite of the boolean value.
'''

x = 5
y = 2
print(x > 2 and y > 2) # True
print(x > 2 or y > 2) # True
print(not(x > 2)) # False


#Using Booleans in Control Structures

#Booleans can be used in control structures such as if, else, and elif to determine the flow of execution.

x = 5
y = 2

if x > y:
    print("x is greater than y")
else:
    print("x is less than or equal to y")
'''
# Output: x is greater than y
In the example above, the if statement checks if the value of x is greater than the value of y. If this is True, the code block within the if statement is executed and the message "x is greater than y" is printed. If the statement is False, the code block within the else statement is executed and the message "x is less than or equal to y" is printed.

Similarly, we can use elif (short for "else if") to check for multiple conditions.
'''
x = 5

if x > 10:
    print("x is greater than 10")
elif x > 0:
    print("x is greater than 0")
else:
    print("x is less than or equal to 0")

# Output: x is greater than 0
'''
In the example above, the first if statement checks if x is greater than 10, which is false. Next, the elif statement checks if x is greater than 0, which is true, so the corresponding block of code is executed and the message "x is greater than 0" is printed.

It's also possible to use and, or and not boolean operators inside the control structures

Summary

In this lesson, we learned about booleans in Python, including what they are, how to create them, and how to use them in control structures. Boolean values are used to represent the truth or falsity of a statement, and are essential for controlling the flow of execution in a program. Practice using booleans, comparison and boolean operators in control structures to gain a deeper understanding of how they work.
'''
