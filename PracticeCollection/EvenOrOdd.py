# A program that accepts 1 integer input and tells you if the number is ODD or EVEN
num = int(input("Type ONE integer to know whether it's EVEN or ODD. "))

if (num % 2) == 0:
  print("{0} is Even.".format(num))
else:
  print("{0} is Odd.".format(num))

a = int(input("\nType an integer value for 'A' to know whether it's bigger or smaller than integer 'B'. "))
b = int(input("Type an integer value for 'B' to know whether it's bigger or smaller than integer 'A'. "))

#2 A program that takes in 2 integers, and tells you which one is the smaller integer of the two.
if a < b:
  print("Integer 'A' is the smallest value.") 
else:
  print("Integer 'B' is the smallest value.")

#3 A program that takes in 3 integers, and returns the middle number.

a = float(input("\nType an integer value for 'A'. "))
b = float(input("Type an integer value for 'B'. "))
c = float(input("Type an integer value for 'c'. "))

if a > b:
  if a < c:
    median = a
  elif b > c:
    median = b
  else: 
    median = c
else:
  if a > c:
    median = a
  elif b < c:
    median = b
  else:
    median = c

print("The middle number is", median)
