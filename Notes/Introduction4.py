#May 14, 2024 -- Lists

#Lists
list = ["a", "b", "c"]
print(list)
print(len(list))

list = ["a", 1, True]
print(list[1]) # prints 1
print(list[-1]) # prints True
print(list[0:2]) # prints 'a', 1

list = ["apple", "cherry"]
if "cherry" in list:
    print("YES")

#Changing item value in list
list = [1, 2, 3]
list[2] = 44 # changes 3 to 44
#list[0:1] = 55 # changes everything to 55

#Inserting Item into List
list = ["coke", "fanta", "sprite"]
list.insert(2, "dr pepper") #inserts dr pepper after fanta
list.append("lemonade") # appends item to end of list

#Append list to list
list = [1, 2, 3]
list2 = [4, 5, 6]
list.extend(list2) #list = [1, 2, 3, 4, 5, 6]

#Remove list item
list = ["banana", "strawberry"]
list.remove("banana") # removes the "banana"
list.append("watermelon")
list.pop(1) # pops the first index out

#Looping through list
list = [1, 2, 3, 4, 5]
for x in list: # for loop
    print(x)

for i in range(len(list)): # for loop with index
    print(list[i])

i = 0
while i < len(list): # while loop
    print(list[i])
    i+=1

#Sorting Lists
list = ["motherboard", "graphics card", "psu"]
list.sort() # sorts alphabetically/numerically
list.sort(reverse = True) # sorts in reverse order

list = ["Tree", "Whale", "car", "motor"]
list.sort(key=str.lower) # sorts while considering case-insensitive sort

#Copy Lists
list1 = [1, 2, 3]
list2 = list1.copy()
#list3 = list(list2)
