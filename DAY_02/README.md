# DAY 02

## Content Review 

1. Types of data
..* String
..* Integer
..* Float
2. `print()` statement to output data
3. `input()` to input data and interact with users
4. `for i in range(n)` to do certain code *n* times
5. `if(a == b):` to run code only under certain conditions
6. `x = 3%2` to assign *x* as the remainder of 3/2.
7. `x = random.randint(min,max)` to assign *x* a random number


## Assignment review

#### Fizzbuzz

Challenges of the Fizzbuzz assignment:
+ Counting up to and including 100
+ Only printing 'fizzbuzz' when a number divisible by both 3 and 5 comes up. The solution here lies in the order of operations - first check if *both* conditions are true, then check if *either* condition is true. 

#### Guessing Game

Challenges of the Guessing Game assignment:
+ input() gives us a string, but to check the guess against our program's number we need an integer. How do we convert?
+ How do we end the program after a successful guess?


What's the minimum number of guesses required to guarantee a win for the player?

## Class Content

1. Printing 2.0 - Example 01_printing2
..* Use `str(myInt)` to convert numbers into strings, and `int(myString)` to convert strings into integers.
..* Note that if the conversion cannot be made, there will be an error.
..* `print("string", end="")` prevents a newline after print.
..* Exercise 01

2. Input 2.0 - Example 02_input2
..* Similarly, `int(input("My Question"))` will convert inputted data to integers. 
..* Exercise 02

3. Loops 2.0 - Example 04_whileloops
..* For loops are great for counting a specified amount, but what if you don't know how long you need to loop for? What if, for example, you wanted to loop a try/except statement until the data is correct. Use `while(condition)` loops.
..* Exercise 03

4. Error handling - Example 04_errorhandling
..* You don't want your program crashing and giving the user crazy red messages if something goes wrong. 
..* Using `try:` and `except:` is a way to hide these errors from your users. 

## In Class Exercises

1. Print checkerboard using for loops
2. Average Grade of Class
3. Average Grade with unknown amount of students
4. Average Grade with unknown amount of students *and* error handling

## Assignment: Guessing Game v2 (see assignments folder)
