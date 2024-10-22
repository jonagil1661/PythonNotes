friends= ["john", "jona", "jonah", "jonas"]

x = 0 

while x < 4:
    print(friends[x])
    x=x+1

##################################################################################

from random import randint

numbers= [0,10,20,30,40]

a = numbers[randint(0,4)]
b = numbers[randint(0,4)]

print(a+b)

##################################################################################

friends = ["john", "jona", "jonah", "jonas"]

y = 0
while y < 4 :
    print("My friends are" + friends[y] + ", " + friends[y+1] + ", "+ friends[y+2] + ", and "+ friends[y+3] + ".")
    
    y = y + 4 

##################################################################################

favorite_songs = ["Sibelius Violin Concerto", "Wieniowski Violin Concerto No. 1", "Elgar Violin Concerto", "Tambourin Chinois", "Devil's Trill Sonata"] 

favorite_artists = ["Pinchas Zukerman", "Itzhak Perlman", "Nathan Milstein", "Ray Chen", "Hilary Hahn"]

print("The piece " + favorite_songs[0] + "was played by " + favorite_artists[0] + "." "The piece " + favorite_songs[1] + " was played by " + favorite_artists[1] + ".""The piece " + favorite_songs[2] + " was played by " + favorite_artists[2] + ".""The piece " + favorite_songs[3] + " was played by " + favorite_artists[3] + ".""The piece " + favorite_songs[4] + " was played by " + favorite_artists[4] + ".")

##################################################################################

items= ["red", "orange", "yellow", "green", "blue"]

print(items)

items.append("purple")
items.append('white')

print(items)

##################################################################################

colors=["red", "orange", "yellow", "green", "blue"]

print(colors)

colors.pop(0)
colors.pop(3)

print(colors) 

##################################################################################

colors = []

input = input("Input your five of your favorite colors and separate each color with a comma and space\n(Ex: 1, 2, 3, 4, 5): ")

colors.append(input)

print("Your favorite colors are: " + str(colors))