"""
Lesson Title: "Understanding and Using While Loops in Python"

Objective: By the end of this lesson, students will be able to understand and effectively use while loops in Python programming.

Materials Needed:

    A computer with Python installed
    
    A text editor or IDE (Integrated Development Environment)
    
    I recommend Sublime Text (https://www.sublimetext.com/)
    
Introduction:

    While loops are a fundamental construct in programming that allow you to repeat a specific block of code while a certain condition is true.

    In Python, while loops are used to repeatedly execute a block of code as long as a certain condition is true.

Syntax:

The basic syntax of a while loop in Python is as follows:
"""
while condition:
    # code to be executed
'''
The condition is the boolean expression that is evaluated before each iteration of the loop. If the condition is true, the code in the loop will be executed. If the condition is false, the loop will exit.
'''
# Example 
# Using a while loop to print the numbers from 1 to 5
i = 1
while i <= 5:
    print(i)
    i = i + 1
'''
Code Walkthrough:

    The i = 1 statement is used to initialize the variable i to 1 before the loop starts.

    The while i <= 5: statement is used to create a loop that will continue as long as the value of i is less than or equal to 5.

    The print(i) statement is used to print the current value of i to the screen.

    The i = i + 1 statement is used to increment the value of i by 1 after each iteration of the loop.

Output:
1
2
3
4
5
######################################################################################################################
Task:

    Create a while loop that repeatedly prompts the user for a password until they enter the correct password.
    Create a while loop that repeatedly generates random numbers between 1 and 100 until it generates the number 42.
Conclusion:

    While loops are a powerful tool for repeating a specific block of code while a certain condition is true.
    Understanding the syntax and usage of while loops is essential for becoming a proficient Python programmer.
Practice:

    Try creating while loops with different conditions and perform different tasks in the loop block.
    Try using break and continue statements within while loops.

Additional Resources:

    Python documentation on while loops: https://docs.python.org/3/tutorial/introduction.html#first-steps-towards-programming
'''
