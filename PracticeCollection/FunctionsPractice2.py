#Function takes parameter radius and calculates circumference.
from math import pi

def circleCircumference(radius):
	c = 2*pi*radius
	return c

r = int(input("Input the radius of your circle: "))

print("The circumference of the circle is: ", circleCircumference(r))

#Function calculates volume of rectangle by l, w, h
def rect_vol():
  v = l*w*h
  return v

l = int(input("Input the length of your rectangular prism: "))
w = int(input("Input the width of your rectangular prism: "))
h = int(input("Input the height of your rectangular prism: "))

print("The volume of the rectangular prism is: ", rect_vol())

# Calculates area & perimeter of rectangle
def area():
  a = l*w
  p = (2*l)+(2*w)
  return a, p

l = int(input("Input the length of your rectangle: "))
w = int(input("Input the width of your rectangle: "))

print("The area and perimeter of the rectangle are (area, perimeter): ", str(area()))

#Calculates grade average
def avgGrade(grades):
	n = len(grades)
	print(n)
	total = 0
	for k in range(n):
		total = total + grades[k]
	average  = total/n
	return average

mygrades = [0,20,40,60,80,100]

myavg = avgGrade(mygrades)

print("\n")
print("Your average grade is: ", myavg)