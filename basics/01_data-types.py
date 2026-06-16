# Python Basics - Essential Data Types and Comments

# Comments in Python
# This is a single-line comment
"""
This is a multi-line comment
or docstring
"""

# Variables - Python is dynamically typed
name = "John Doe"
age = 30

# Strings
first_name = "Alice"
last_name = "Smith"
full_name = first_name + " " + last_name  # String concatenation
print(f"Full name: {full_name}")  # f-strings (formatted strings)

# String methods
text = "Hello World"
print(text.upper())  # HELLO WORLD
print(text.lower())  # hello world
print(text.replace("World", "Python"))  # Hello Python
print(len(text))  # Length of string: 11

# Numbers - Integers
x = 10
y = 5
print(x + y)  # Addition: 15
print(x - y)  # Subtraction: 5
print(x * y)  # Multiplication: 50
print(x / y)  # Division: 2.0
print(x // y)  # Floor division: 2
print(x % y)  # Modulus: 0
print(x ** y)  # Exponentiation: 100000

# Numbers - Floats
pi = 3.14159
radius = 5.0
area = pi * (radius ** 2)
print(f"Area of circle: {area:.2f}")

# Boolean
is_active = True
is_deleted = False
print(type(is_active))  # <class 'bool'>

# Type conversion
num_str = "100"
num_int = int(num_str)  # String to integer
num_float = float(num_str)  # String to float
print(f"Integer: {num_int}, Float: {num_float}")

# Multiple assignment
a, b, c = 1, 2, 3
print(a, b, c)

# Constants (by convention, use UPPERCASE)
PI = 3.14159
MAX_SIZE = 100

# Basic input/output
# user_name = input("Enter your name: ")
# print(f"Hello, {user_name}!")

# Check data types
print(type(name))  # <class 'str'>
print(type(age))  # <class 'int'>
print(type(pi))  # <class 'float'>