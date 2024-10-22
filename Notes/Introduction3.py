#May 14, 2024 -- Booleans and operators and Lists

#Boolean statements/conditions
print(10 > 3) # prints True

if 10 > 4:
    print("Yay")
else:
    print("Aww")

# bool()
print(bool("Hello"))
print(bool(15))

print(bool("")) # prints False b/c string is empty
print(bool(0)) # prints False b/c int is 0

#Functions can return a boolean
def myfunction():
    return True
print(myfunction())

if myfunction():
    print("True")
else:
    print("False")

#Operators
x = 1 + 3 - 5 * 5 / 3 % 7
x += 5
x /= 6
x /= 1.4
x = x ** 2 #exponentiation

#Comparison Operators
if 1==1:
    print("yes")
elif 1 != 1:
    print("no")
elif 1 >= 5:
    print("kind of")

#Logical operators
if 1>4 and 4<5:
    print("break")
elif 2==4 or 1==1:
    print("hello")
elif not(2>5):
    print("world")




