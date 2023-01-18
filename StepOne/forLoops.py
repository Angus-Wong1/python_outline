"""
Lesson Title: "Mastering Python For Loops"

Objective: By the end of this lesson, students will be able to understand and effectively use for loops in Python programming.

Materials Needed:

    A computer with Python installed
    A text editor or IDE (Integrated Development Environment)
    I recommend sublime text(https://www.sublimetext.com/)
    
Introduction:

    For loops are a fundamental construct in programming that allow you to repeat a specific block of code for a certain number of times or until a certain condition is met.

    In Python, for loops are used to iterate over a sequence of items, such as a list, tuple, or string.

Syntax:

The basic syntax of a for loop in Python is as follows:
"""
    for variable in sequence:
        # code to be executed
        # end of code
#The variable is the name of the variable that will take on the value of the current item in the sequence during each iteration.
#The sequence is the collection of items that the loop will iterate over.

#Example of for loop code:
# Using a for loop to print the numbers from 1 to 5
for i in range(1, 6):
    print(i)
"""
Code Walkthrough:
The for i in range(1, 6) statement is used to create a loop that will iterate over the numbers from 1 to 5.

The variable i is used to store the current value of the item in the sequence during each iteration.

The print(i) statement is used to print the current value of i to the screen.

Output:
1
2
3
4
5

######################################################################################################################

TRY IT YOURSELF

    Task:

    Create a for loop that iterates over a list of fruits and prints each one to the screen.
    Create a for loop that iterates over a range of numbers and prints the square of each number to the screen.
    Conclusion:

    For loops are a powerful tool for repeating a specific block of code for a certain number of times or until a certain condition is met.
    Understanding the syntax and usage of for loops is essential for becoming a proficient Python programmer.
    Practice:

    Try creating for loops with different sequences and perform different tasks in the loop block.
    Try using break and continue statements within for loops.
    Additional Resources:

    Python documentation on for loops: https://docs.python.org/3/tutorial/controlflow.html#for-statements
    
    
  """
