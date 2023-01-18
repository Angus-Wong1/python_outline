'''
Lesson Title: "Mastering Python Functions"

Objective: By the end of this lesson, students will be able to understand and effectively create and use functions in Python programming.

Materials Needed:

  A computer with Python installed
  
  A text editor or IDE (Integrated Development Environment)
  
  I recommend sublime text(https://www.sublimetext.com/)

Introduction:

  Functions are a fundamental construct in programming that allow you to organize and reuse code.

  In Python, functions are defined using the def keyword and can take parameters and return values.

Syntax:

The basic syntax of a function in Python is as follows:
'''
def function_name(parameters):
    # code to be executed
    return value
'''
  The function_name is the name of the function, which should be a descriptive and meaningful name.

  The parameters are the variables that are passed to the function as input.

  The return value is the value that the function returns to the caller.
'''
#Example:
# Defining a function to find the square of a number
def square(num):
    return num * num

# Using the function
result = square(5)
print(result)
'''
Code Walkthrough:

  The def square(num): statement is used to define a new function named square that takes a single parameter num.

  The return num * num statement is used to return the square of the num parameter.

  The result = square(5) statement is used to call the square function and pass the value 5 as the num parameter.

  The print(result) statement is used to print the result of the function call to the screen.

Output:
25

######################################################################################################################

Task:

  Create a function that takes two numbers as parameters and returns their sum.
  
  Create a function that takes a list of numbers as a parameter and returns the largest number in the list.

Conclusion:

  Functions are a powerful tool for organizing and reusing code.

  Understanding the syntax and usage of functions is essential for becoming a proficient Python programmer.

Practice:

  Try creating different functions with different parameters and return values.

  Try using functions within other functions.

Additional Resources:

  Python documentation on functions: https://docs.python.org/3/tutorial/controlflow.html#defining-functions
'''
