import random

#Prints random character from list
superheroes=["Superman", "Batman", "Wonderwoman", "Green Lantern", "Aquaman"] 
x = random.randint(0,4)
print(superheroes[x])

#Appends characters to list
characters = ["bugs bunny", "sylvester", "tweety", "porky pig", "tasmanian devil"]
n = 0
while n<5: 
  superheroes.append(characters[n])
  n=n+1
  if n==5: 
    print(superheroes)
    break

#Removes any name, from your list of 10 characters, that is longer than 9 letters (including the space). 
for x in range (0,len(superheroes),1):
  if x<len(superheroes):
    if(len(superheroes[x])>9):
      superheroes.pop(x)
print(superheroes)

#Sorts the list in ascending order, calculates the average of all the grades.
grades = [94, 65, 72, 50, 100, 94, 83]
grades.sort()
print("Grades (sorted in ascending order):" + str(grades))
avggrades=float((94+65+72+50+100+94+83)/7)
print("Grades (Averaged):" + str(avggrades))