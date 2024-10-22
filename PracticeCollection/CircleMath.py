#Functions to call particular color named functions to execute the relevant ANSI Escape Sequence.
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))

#Colored Output statement introducing the program.
prCyan("Program Introduction:\nThis program will separately solve two different equations by utilizing two math. functions based on a real world situation.\nThe user will input a certain value that the program will use to solve the equations.\nThe program will output two final values.\nIt will then output a final statement displaying the two final answers rounded to the nearest 2nd decimal point.") 

#Importing 2 functions from imported Math Module.
import math
from math import pi
from math import degrees

#Output asking the user to input a value for the variable 'radius'.
radius = input("Please enter a value/integer: ") 

#Output statement introducing the 'real life' situation involving math applications.
print("\nReal-life Situation:\nLittle Johnny had a whole pie with a radius of " + radius + " feet.\nHe wants to cut the pie into 20 slices.\nUsing the circumference and area formula of a circle, respectively, he wants to figure out the arc length and area of each slice he cut out to two decimal places.\n") 

#Fun output statement asking the users to input their decision on whether or not 
# they would like to know the final answers.
input("Would you like to know the final answers? ") 

#Output statement introducing the 'Final answers'.
print("\nFinal answers:") 

#Arc/circumference calculation involving the input radius value, 
# based on the equation: 2rπ; this subsitutes for the variable 'arc' (uses math.pi!).
arc = int(radius) * pi/10 

#Output statement giving the unrounded value of the arc/circumference.
print("Arc length/circumference = " + str(arc) + " ft.") 

#Variable to substitute for r².
sqrad = int(radius) * int(radius) 
#Area calculation involving the input radius value, based on the equation: πr², 
# involving the input radius value; this substitutes for the variable 'area' (uses math.degrees()!).
area = pi * int(sqrad) * degrees(pi/10) / degrees(2*pi) 

#Output statement giving the unrounded value of the area.
print("Area = " + str(area) + " ft.\n") 

#Final output statement stating the area and arc/circumference values for one 
# slice of pie (rounded to the 2nd decimal place).
prLightPurple("Final Statement: (rounded to 2nd decimal place)\nThe length of an arc\
     for one slice is " + str(round(arc,2)) + " ft, and the area of one slice is " + str(round(area,2)) + " ft.") 