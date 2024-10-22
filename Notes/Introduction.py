# May 14, 2024 -- Print, Variables, Casting, Data types Notes

print("Hello, World!")

# This line is a comment

"""
This whole
block is a 
comment !!!
"""

x = 5
y = "Hello, World!"

print(x) # Prints 5
print(y) # Prints "Hello, World!"

#print (x + y) # Error b/c str and int are incompatible

#Casting
x = str(3) # x will be '3'
y = int(3) # y will be 3
z = float(3) # z will be 3.0

print(type(z)) # Prints data type class of z

#Case sensitive
a = 4
A = 15 # A won't overwrite a

"""
Variable Names Rules:
1. Must start with letter or _
2. Can't start with number or anything else
3. Can only contain alpha-numeric characters & underscores
4. Names are CASE-SENSITIVE
"""

x, y, z = "ste", "pha", "nie"
print(x + y + z) # Prints 'stephanie'
print(x,y,z) # Prints 'ste pha nie'

x = y = z = "stephanie" # x, y, z are all "stephanie"

#Unpacking from a list
list = [1, 2, 3]
x, y, z = list # x is 1, y is 2, z is 3

#Global Variables
x = 3
def myfunction():
    print(x)
myfunction()

#Global Keyword
def myfunction1():
    global x1
    x1 = 3
myfunction1()
print(x1) # Prints 3

#Global Keyword to change
x2 = 66 
def myfunction2():
    global x2
    x2 = 3
myfunction2()
print(x2) # Prints 3

"""
Data Types
Text: str
Numeric: int, float, complex
Sequence: list, tuple, range
Mapping: dict
Boolean: bool
Binary: bytes, bytearray
None: NoneType 
"""

x = "Hello, World!" # str
x = 20 # int
x = 20.5 # float
x = [1, 2, 3] # list
x = (1, 3, 5) # tuple
x = range(5) # range
x = True # bool
x = None # NoneType

x = str("Hello, World!") # str
x = int(20) # int
x = float(20.5) # float
#x = list(("apple", "banana", "cherry")) # list
x = tuple((1, 3, 5)) # tuple
x = range(6) # range
x = bool(5) # bool

#Random
import random
print(random.randrange(1, 10)) # Prints random number from 1 - 9

#Type Casting
x = int(1) # x is 1
x = int(2.6) # x is 2 (rounds to floor)
x = int("3") # x is 3

y = float(1) # y is 1.0
y = float(3.6) # y is 3.6
y = float("4") # y is 4.0
y = float("4.6") # y is 4.6

#Multiline String to variable
x = """ I love
eating cherries
and strawberries!"""

#Strings are arrays
a = "Hello, World!"
print(a[0]) # Prints 'H'