#May 14, 2024 -- Classes, Inheritance, Polymorphism

#__init__() function
class Person:
    def __init__(self, name, age): #__init__() is initiated as soon as object is made
        self.name = name
        self.age = age
p1 = Person("Johnny", 44)
print(p1.name) # Prints 'Johnny'

#Inheritance with parent/child classes
class Animal: # parent class
    def __init__(self, name):
        self.name = name
    def printname(self):
        print(self.name)

class Cat(Animal): # child class inherits properties of parent
    def __init__(self, name, color): # the child's __init__() overrides the parent's
        super().__init__(name) # super() makes child inherit all properties from parent
        self.tails = 1
        self.color = color

x = Cat("Cathy", "red")

