# "r" - read (default value)
# "w" - write (opens file for writing)
# "x" - create (creates specified file)
# "a" - append (appends to end of file)
# "w" - writes over existing content in file

file1 = open("FileReading1.txt", "r")
print(file1.read()) # prints "Hello, World!"
file1.close()

file1 = open("FileReading1.txt", "r") # requires another open() function to use read() method again
print(file1.read(5)) # prints "Hello"
file1.close()

file2 = open("FileReading2.txt", "r")
print(file2.readline()) # prints first line in file
print(file2.readline()) # prints second line in file as well
file2.close() # good practice to close files after finishing

file2 = open("FileReading2.txt", "r")
for x in file2: # loop through each line in file to read entire file
    print(x)
file2.close() # good practice to close files after finishing

file1 = open("FileReading1.txt", "a")
file1.write("Hello, World!\n") # write at end of file
file1.write("Hello, World!")
file1.close()

file1 = open("FileReading1.txt", "r")
print(file1.read())
file1.close()

import os # OS module
if not os.path.exists("FileReadingDemo.txt"):
    x = input("Would you like to create a new file? (y/n): ")
    if x is "y":
        file3 = open("FileReadingDemo.txt", "x")
        file3 = open("FileReadingDemo.txt", "w")
        file3.write("This is a demo file that will be deleted...")   

if os.path.exists("FileReadingDemo.txt"):
        x = input("Would you like to delete FileReadingDemo.txt? (y/n): ")
        if x is "y":
            print("Path exists... Now deleting...")
            os.remove("FileReadingDemo.txt")
else:
    file3 = open("FileReadingDemo.txt", "r")
    print(file3.read())
    print("File doesn't exist")