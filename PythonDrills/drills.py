# Python drills

import math 

# Print statement 
"""
print("Hi im Petar")
print('*' * 10)
"""

# Variable usage
"""
price = 10
print(price)

patient_name = "John Smith"
patient_age = 20
patient_new = True
print(patient_name)
print(patient_age)
print(patient_new)
"""

# Input usage
"""
name = input('What is your name? ')
surname = input('What is your surname? ') 
print('Hi ' + name + ' ' + surname + '!')
"""
"""
birth_year = input('What is your birth year? ')
age = 2025 - int(birth_year)
print(age)
"""

# String vs formatted string and string methods and functions
"""
first = 'John'
last = 'Smith'
message1 = first + ' [' + last + '] is a coder'
print(message1) 
message2 = f'{first} [{last}] is a coder' # This is formatted string f'...', and it is used as more readable option
print(message2)
print(first.lower())
print(len(last))
"""
# If statements
"""
is_hot = False 
is_cold = False
if is_hot:
    print('It is a hot day, drink some water!')
elif is_cold:
    print('It is a cold day, wear warm clothes!')
else:
    print("Enjoy your day!")

"""
"""
name = input("Enter your username: ")
length = len(name)
if length < 3:
    print("Username must be longer than 3 characters!")
elif length > 50: 
    print("Username must be shorter than 50 charachters!")
else:
    print(f'Welcome back {name}')

"""

# While loop
"""
while i <= 5:
    print('*' * i)
    i = i + 1
print("Done")
"""

# For loop - Indexable For loop that can have both index and symbol that are incrementing
"""
for item in ['John', 'Sarah', 'Jack']: # here can be anything, string,char,int...
    print(item)

for item in range(10): # also can , range(5,10) , range(5,10,2) where 2 is incrementation value
    print(item)

s = "HelloWorld"
for i, letter in enumerate(s):
    print(f'Index: {i} Letter: {letter}')

# Nested loops - example - print out coordinates and challenge 1
"""
"""
for x in range(4):
    for y in range(4): 
        print(f"({x},{y})")

numbers = [1,1,1,1,4] # print L with x's withous using one for loop and 'x' * i
string_to_write = ""
for i in numbers:
    for j in range(i):
        string_to_write += 'x'
    print(string_to_write)
    string_to_write = ""
"""

# Lists

"""
names = ['John' , 'Jack', 'Bob', 'Sarah', 'Mosh']
print(names)        # entire lists including [] and ''
print(names[0])     # first element 
print(names[-2])    # second from back element
print(names[2:4])   # range lists from 3rd to 5th element

names[0] = 'Jon'    # modify the certian element
print(names)

# some list methods
numbers = [5,2,1,6,7]
numbers.append(14)
numbers.insert(2,15)
numbers.pop()  # removes the last element
print(numbers.index(1)) # or print (1 in numbers)
print(numbers.count(14))
print(numbers)
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
numbers2 = numbers.copy() # creates a copy
print(numbers2)
"""

# Two-dimensional lists - matrix here is a list with lists as elements
"""
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0][2])

for row in matrix:
    for item in row:
        print(item)
"""

# Tuples - lists that can not modify elements, we can only get information about a tuple
"""
coordinates = (1,2,3)

x = coordinates[0]
y = coordinates[1]
z = coordinates[2]

# this is called unpacking and the results is same as above, less code neccesary! Works with lists aswell
x,y,z = coordinates
"""

# Dictionary - structures that saves data in key-value format
"""
customer = {
    "name" : "John Smith",
    "age"  : 30,
    "is_verified" : True
}

customer["birthdate"] = "Jan 1 1989"
print(customer["name"])     # if there is no such key, error is issued
print(customer.get("name", "John Doe")) # this way we recieve a none value, in case no such key exists. We can set a default value for a non-existing key
"""
# Multi-value dictionary - List of dictionaries 

# Every student is a dictionary
students = [
    {"name" : "Hermione" , "house":"Gryffindor" , "patronus" : "Otter"},
    {"name" : "Harry" , "house":"Gryffindor" , "patronus" : "Stag"},
    {"name" : "Ron" , "house":"Gryffindor" , "patronus" : "Jack Russell terries"},
    {"name" : "Draco" , "house":"Slytherin" , "patronus" : None},
]

for student in students:
    print(student["name"], student["house"],student["patronus"], sep=",")

# Functions 
"""
def greet_user(first_name,second_name):
    print(f"Greetings {first_name} {second_name}!")
    print("Welcome!")

greet_user("John", "Doe")                               # positional arguments
greet_user(first_name="Sarah", second_name="Danger")    # keyword argument

def square(number):
    return number * number

print(square(8)) 
"""

# Exceptions
"""
try:
    age = int(input("Age: "))
    income = 20000
    risk = income/age
    print("Age: " + age)
    print("Risk: " + risk)
except ValueError: 
    print("Inavlid value. Age must be a number!")
except ZeroDivisionError:
    print("You can not divide with zero!")
"""

# Classes - Defining new types and its methods
"""
# Example 1
class Point:
    def __init__(self, x, y):
        self.x = x 
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")
 

point1 = Point(10,20)
print(point1.x)
point1.x = 11
print(point1.x)

# Example 2
class Person:
    def __init__(self,name):
        self.name = name
    
    def talk(self):     # Self is a pointer to an object
        print(f"Hello, my name is {self.name}!")

person1 = Person("John")
person1.talk()
"""

# Inheritance 

"""
class Mammal: 
    def walk(self):
        print("walk")

class Dog(Mammal):
    def bark(self):
        print("Woof!")           

class Cat(Mammal):
    pass                     # pass means simply ignore the line

max = Dog()
max.walk()
max.bark()
"""

# Generating random values
"""
import random

for i in range(3):
    print(random.random())
    print(random.randint(10,20))

members = ["John", 'Mary', "Bob", "Josh"]
leader = random.choice(members)
print(leader)
"""

# Working with files and directories

"""
from pathlib import Path

## Absolute path
# C:\Program Files\... 

## Relative path
path = Path("ecommerce")
print(path.exists())
path = Path()
print(path.glob('*.py'))
for file in path.glob('*.py'):  # lists out all of the .py files, for ALL files write *.*
    print(file)
"""