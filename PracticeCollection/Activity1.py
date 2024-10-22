#While loop 1
n = 0
while n >= 0:
  n=n+1
  if  n < 6:
    print("I Love ")
  elif n==6:
    print("New York.")

#For loop 1
for n in range(0,5,1) :
  print("I Love")
print("New York")

#While loop 2
n=0
while n<80:
  n=n+4
  print(str(n))

#For loop 2
n = 0
for n in range (4,84,4):
  print(str(n))

#While loop 3
user = str(input("Enter your username: "))
n = 2
while n >= 0:
  if user == "SuperGiraffe007&":
    print("\nWelcome!")
    n -= 1
  elif user == "SUPERGIRAFFE007&": 
    print("\nWelcome!")
    n -= 2
  elif user == "Supergiraffe007&":
    print("\nWelcome!")
    n -= 3
  elif user == "superGiraffe007&":
    print("\nWelcome!")
    n -= 4
  elif user == "supergiraffe007&":
    print("\nWelcome!")
    n -= 5
  if n > 0:
    print("\nIncorrect username. Try again.")
    user = str(input("\nEnter your username: "))
  n = n - 1
  if n==0:
    print("Out of attempts. You are locked out.")

#For loop 3
user = str(input("Enter your username: "))
for n in range (1,4,1):
  if user =="SuperGiraffe007&" or user=="supergiraffe007&" or user=="Supergiraffe007&" or user=="superGiraffe007&" or user=="SUPERGIRAFFE007&":
    print("\nWelcome!")
    break
  if n<3:
    print("\nIncorrect username. Please try again.")
    user=str(input("\nPlease enter your username: "))
  if n==3:
    print("Out of attempts. You are locked out.")

#While loop 4
n = 5
answer = 0
pswd = 4778
while pswd!= answer and n > 0:
  answer = int(input("Enter the four digit password: "))
  n -= 1
  if answer < pswd:
    print("Sorry, try again!")
  elif answer > pswd:
    print("Sorry, try again!")
  else:
    print("That’s it!")
if answer != pswd:
  print("Out of attempts. You are locked out.")

#For loop 4
user = str(input("Enter the four digit password: "))
for n in range (1,6,1):
  if user == str(4778) :
    print("\nThat’s it!")
    break
  if n<5:
    print("\nSorry, try again!")
    user=str(input("\nPlease enter your username: "))
  if n==5:
    print("Out of attempts. You are locked out.")

#While loop 5
n = 13
a, b = 0, 1
count = 0
print("All numbers in the Fibonacci sequence under 200")
while count < n:
    print(a)
    c = a + b
    a = b
    b = c
    count += 1

#For loop 5
N = 13
fibonacci = [0,1]

if N>2:
	for i in range(2, N):
		nextElement = fibonacci[i-1] + fibonacci[i-2]
		fibonacci.append(nextElement)

print(fibonacci)