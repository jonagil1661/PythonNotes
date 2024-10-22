# May 14, 2024 -- Loops and Strings

#For loop
for x in "stephanie":
    print(x) #loops through each letter and prints each on a line

#String length
x = "Hello, World!"
print(len(x)) # Prints the length
print(len("Hello, WOrld!")) # Does the same

#Check String
txt = "The small cat ran over the dog."
print("dog" in txt) # in is used to check if word is in string

if "small" in txt:
    print("YAY")

# Check if NOT
txt = "I love tomatoes"
print("love" not in txt) # Prints false

#Slicing
x = "Hello, World!"
print(x[2:8]) # Prints 'llo, W'
print(x[-4:-2]) # Prints 'rl'

#Upper and Lower Case
x = "Hello, World!"
print(x.upper())
print("HELLO".lower()) # prints 'hello'
print("hello, world!".upper()) # prints 'HELLO, WORLD!'

#Replace
x = "Hello, World!"
print(x.replace("H", "J")) # prints Jello, World!

#String Concatenation
x, y = "Hello", "World"
z = x + y
print(z) # prints 'HelloWorld'

#F-Strings
age = 78
txt = f"My name is grandpa, I am {age} years old"

#Placeholders with modifiers
price = 23
txt = f"The price of this banana is {price:.2f} dollars" # Displays price with 2 decimals

print(f"This is a calculation of {38 * 1}") 

#Backslash
print("We are the \"Monster\" corporates") # Using quotes in Strings
print("Tab\tTab")

