import turtle

turtle.speed(500) 
turtle.penup()  
turtle.color("#1fb68c")  

def hexagon():
  import turtle
turtle.goto(0,-100)  #Drawing the hexagon
turtle.begin_fill()
turtle.circle(100, steps=6.0)  
turtle.end_fill()

def circle():
  import turtle
turtle.color('white')  #Circle with white filled in
turtle.sety(20)  
turtle.begin_fill()
turtle.circle(20)  
turtle.end_fill()

def petals():
  import turtle
turtle.forward(60)
turtle.right(85)
turtle.begin_fill() #Leaf looking things
turtle.circle(-60, 190)
turtle.right(85)
turtle.circle(-60, 90)
turtle.left(180)
turtle.circle(-60, 90)
turtle.end_fill()

def text(): #Writes name of logo; khan academy
  import turtle
  turtle.goto(0,-150)
  turtle.color("#1fb68c")
  turtle.write("Khan Academy", align="center", font=("Times New Roman",60,"bold"))

#Drawing Functions
hexagon() 
circle()
petals()
text()