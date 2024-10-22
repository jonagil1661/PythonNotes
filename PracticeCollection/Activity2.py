from math import pi

def circleArea(r) :
  a = pi * r * r
  return a

r = int(input("Please input the radius of your circle to solve for the area: "))

print("The area of your circle is: ", circleArea(r))

##################################################################################

def rectangleArea(l, w) :
  a = l * w
  return a

l = int(input("Please input the length of the rectangle to solve for the area: "))
w = int(input("Please input the width of the rectangle to solve for the area: "))

print("The area of your rectangle is: ", rectangleArea(l, w))

##################################################################################

def  perimeter(y, x) :
  p = (2*y) + x + (0.5*pi*x)
  return p

def area(y,x) :
  a = (y*x) + ((x/2)*(x/2)*pi*0.5)
  return a

y = int(input("Please input the y value of your figure: "))
x = int(input("Please input the x value of your figure: "))


print("The area of your figure is: ", area(y, x))
print("The perimeter of your figure is: ", perimeter(y, x))

##################################################################################

def pizzaPerimeter(d, l) :
  p = l + l + (pi*d*0.5)
  return p

def pizzaArea(d, l) :
  a = (0.5*pi*(d/2)*(d/2) + (0.5 * d * ((l**2) - ((d/2)**2)**(1/2))))
  return a

d = int(input("Please input the d value of your figure: "))
l = int(input("Please input the l value of your figure: "))

print("The area of your figure is: ", pizzaArea(d, l))
print("The perimeter of your figure is: ", pizzaPerimeter(d,l))

##################################################################################

def volume(r) :
  v = 4/3*pi*r*r*r
  return v

def surfacearea(r) :
  sa = 4*pi*r*r
  return sa

r = int(input("Please input the r value of your sphere: "))

print("The volume of your figure is: ", volume(r))
print("The surface area of your figure is: ", surfacearea(r))

##################################################################################

prices = []

numItems = int(input("How many items did you purchase?: "))

for n in range (0,numItems) :
  itemPrice = float(input("What is the price of item #"+ str(n+1)+ "? $"))
  prices.append(itemPrice)

total = sum(prices)

def price(total) :
   totaltax = 0.07 *total
   rounded_totaltax = "{:.2f}".format(totaltax)
   return rounded_totaltax

print("The tax on this bill is $", price(total))