'''
Lesson Title: "Mastering Python Branching Statements"

    Objective: By the end of this lesson, students will be able to understand and effectively use branching statements in Python programming, such as if, elif, and else.

Materials Needed:

    A computer with Python installed
    
    A text editor or IDE (Integrated Development Environment)
       
     I recommend sublime text(https://www.sublimetext.com/)

Introduction:

    Branching statements are a fundamental construct in programming that allow you to make decisions based on certain conditions.

    In Python, branching statements are used to execute different code blocks depending on the outcome of a certain condition.

Syntax:

    The basic syntax of an if statement in Python is as follows:
'''
if condition:
    # code to be executed if condition is true
# The elif and else statements are used to add additional conditions and code blocks.

elif condition:
    # code to be executed if the previous conditions were false and this condition is true
else:
    # code to be executed if all previous conditions were false

#Example:
# Using an if statement to check if a number is positive, negative, or zero
num = 0
if num > 0:
    print("Positive Number")
elif num < 0:
    print("Negative Number")
else:
    print("Zero")
    
'''
Code Walkthrough:

    The num = 0 statement is used to initialize the variable num to 0.

    The if num > 0: statement is used to check if the value of num is greater than 0. If the condition is true, the code inside the if block will be executed.

    The elif num < 0: statement is used to check if the value of num is less than 0. If the previous conditions were false and this condition is true, the code inside the elif block will be executed.

    The else: statement is used to specify code that will be executed if all previous conditions were false.

Output:

Zero

######################################################################################################################
Task:

    Create an if-elif-else statement to determine if a number is even or odd.
    
    Create an if-elif-else statement to determine if a given character is a vowel or a consonant.
    
Conclusion:

    Branching statements, such as if, elif, and else, are a powerful tool for making decisions and controlling the flow of a program.

    Understanding the syntax and usage of branching statements is essential for becoming a proficient Python programmer.

Practice:

    Try creating different branching statements and test them with different conditions.

    Try using logical operators (and, or, not) in conditions to create more complex branching statements.

Additional Resources:

Python documentation on branching statements: https://docs.python.org/3/tutorial/controlflow.html#if-statements

'''
