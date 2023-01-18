'''
Lesson Title: "Mastering Python Scoping"

    Objective: By the end of this lesson, students will be able to understand and effectively use scoping in Python programming.

Materials Needed:

    A computer with Python installed
    
    A text editor or IDE (Integrated Development Environment)
    
    I recommend sublime text(https://www.sublimetext.com/)
    
Introduction:

    Scoping is the mechanism by which a programming language determines which variables are accessible to which parts of a program.
    
    In Python, variables defined within a function are local to that function and are not accessible outside of it, while variables defined outside of a function are global and accessible from anywhere within the program.

Example:
'''
# Declaring a global variable
x = 5

def func():
    # Declaring a local variable
    y = 10
    print(x)
    print(y)

func()
# uncomment line 33 to see error 
#print(y) 
'''
Code Walkthrough:

    The x = 5 statement is used to define a global variable x with the value 5.

    The def func(): statement is used to define a new function named func.

    The y = 10 statement is used to define a local variable y with the value 10 within the function func.

    The print(x) statement is used to print the value of the global variable x to the screen.

    The print(y) statement is used to print the value of the local variable y to the screen.

    The func() statement is used to call the func function.

    The print(y) statement is used to print the value of the local variable y to the screen, but it will raise an error because the variable is not defined outside the function.

Output:
5
10
NameError: name 'y' is not defined

######################################################################################################################

Task:

    Create a global variable and a local variable with the same name and see what happens when you try to access them inside and outside a function.
    
    Try to modify a global variable within a function and see what happens when you try to access it outside the function.

Conclusion:

    Scoping is an important concept in programming that allows you to control the accessibility of variables.
    
    Understanding the scoping rules in Python is essential for becoming a proficient Python programmer.

Practice:

    Try creating different variables with different scopes and test their accessibility.
    
    Try using the global keyword to access and modify global variables within a function.

Additional Resources:

Python documentation on scoping: https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces
'''
