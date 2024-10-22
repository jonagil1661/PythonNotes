#WRITE A FUNCTION THAT RANDOMLY PRINTS OUT 2 RANDOM LETTERS FROM THE ALPHABET AND A 2-DIGIT NUMBER (ex: TN23). THEN CALL THE FUNCTION 3 TIMES ON THE LAST LINE OF YOUR CODE.

from random import randint

def pract1():
  alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

  a = randint(0, 25)
  b = randint(0, 25)
  num = str(randint(10, 99))

  print(alphabet[a] + alphabet[b] + num)

pract1()
pract1()
pract1()