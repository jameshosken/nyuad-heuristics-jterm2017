# DAY 01

I'm James, your instructor for JTerm. I graduated from NYUAD 2 years ago with a major in film. When I'm not supporting this JTerm course I am the lab manager for the Interactive Media lab in the Arts Center, where we try to blend the tools of computer science, engineering, and art together.

Aside from my major path and current work, I'm interested in Visual Effects & Animation, and Space as humanity's next challenge.

## About Python

+ Python is a "human readable" programming language (as opposed to machine code, or a collection of mathematical symbols, or even binary). 
+ It is compiled at runtime, meaning another program takes all your code and 'translates' it into machine code *before* running it.
+ It is an indented language, meaning whitespace is important. Empty, or tabbed, spaces indicate different blocks of code.


### Non-CS-Specific Python Project Links

[Literature](https://opensource.com/business/15/10/jane-austen-on-python)

[Econ](http://quant-econ.net/)

[More Econ](http://francescopochetti.com/stock-market-prediction-part-introduction/)

[VisArts](https://processing.org/)

[Philosophy](http://www.amazon.com/Monty-Python-Philosophy-Popular-Culture/dp/0812695933)

[Finally](http://www.skilledup.com/articles/reasons-to-learn-python)

## Class content 

#### Python names

A 'name' in python is a sort of container for different types of things (numbers, letters, words). You can assign the number 2 to a name, for example, by typing `mynumber = 2`. Some different types of things than can be attached to a name are:

1. Strings. Any letter, number, or punctuation mark. Identified by single or double quotes. Example: "abcDEF123!@#"
  - You can add strings together using '+'. For example: `"Hello" + "World"` becomes `"HelloWorld"`
2.Integers: Whole numbers. Example: 123
  - You can use mathematical operations on integers. Some common ones are + - / *
  - Note that if you divide an integer by another integer, the answer will be cut off after the decimal point.
3. Floating point numbers ('floats' for short). A number with a decimal point. Examples: 1.23, 0.001, 42.0
  - You can use mathematical operations on floats as well. 
  - Note that if you add/subtract/divide/multiply a float with an integer, the answer will be given as a float.

#### Counting with computers.

`for i in range(100):
	print(i)`

+ Computers count from 0.
+ when using the `range(n)` function, python will count from zero up to, but *not including* n.
+ if you don't want to start from zero, you can use `range(start, stop)`

#### Controlling your program with logic

"If statements" are a way for your program to choose different paths of behaviour based on certain conditions. For example, if you want your program to only respond to a specific username, an if statement would be a great way to make this happen.

```python
if(username == "Luke"):
	print("Hello, Luke")
else:
	print("Go away")
```

Use `and` and/or `or` to add extra finesse to your if statements:

```python
if(username == "Luke" or username == "Leia"):
	print("May the force be with you.")
else:
	print("Move along, stranger.")
```

#### Random

To make use of random number generation in python, you first need to import the random library"

```python
import random
```

Then, when you need a random integer, use:

```python
randomnumber = random.randint(min, max)
```

#### Examples in 'Contents' folder

1. Printing. Example 01_helloworld demonstrates basic syntax of python and outputting data to the console.
2. Input. Example 02_input demonstrates how a user can interact with your program via the console.
3. Counting. Example 03_counting demonstrates using a for loop to iterate through a range of numbers.
4. Conditionals. Example 04_conditionals demonstrates the basics of logic in python. It shows how you can choose different behavioural paths for your program based on certain conditions.
5. Modulo: Example 05_Moludo demonstrates the use of the *modulo* operater, which divides the first number by the second, and then outputs the *remainder of that division*. It is useful for finding odd and even numbers, amongst other things.
6. Patterns. Example 06_patterns is a collection of the patterns drawn during the in-class exercise.