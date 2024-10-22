#Imports a random integer function.
from random import randint 

def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
prPurple("In this 2 player random number guessing game, Player 1 and Player 2 will attempt to guess the correct number between 1-10 one at a time. For each correct guess, the player will be awarded one point. The first player to 5 points wins. Have fun!! \n")

n = randint(1,10) 
guess1 = int(input("Player 1, guess the correct number from 1-10: "))
guess2 = 0

#Sets the initial player scores equal to zero.
player1 = 0 
player2 = 0

#Defines printcolors.
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk)) 
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk)) 

 #A whileloop that keeps on repeating when a player's score is less than 5.
while player1 <= 5 or player2 <= 5 :
  #If Player 1's guess is < the random number: Tells player(s) to guess higher; asks for Player 2's guess input.
  if guess1 < n :
    prRed("Guess higher.")
    prCyan("Player 2, guess the correct number from 1-10: ")
    guess2 = int(input())
    player1 = player1
  
  #If Player 1's guess is > the random number: Tells player(s) to guess lower; asks for Player 2's guess input.
  elif guess1 > n :
    prRed("Guess lower.")
    prCyan("Player 2, guess the correct number from 1-10: ")
    guess2 = int(input())
    player1 = player1
  
  #If Player 1's guess is = the random number: Awards Player 1 with 1 pt; asks for Player 1's guess input.
  else :
    player1 = player1 + 1
    prGreen("\nScore: Player 1 = "+str(player1)+" pts | Player 2 = "+str(player2)+" \n")
    guess1 = 0
    n = randint(1,10)
    guess2 = int(input("Player 2, guess the correct number from 1-10: \n"))
  
  #If Player 2's guess is < the random number: Tells player(s) to guess higher; asks for Player 1's guess input.
  if guess2 < n :
    prRed("Guess higher.")
    guess1 = int(input("Player 1, guess the correct number from 1-10: \n"))
    player2 = player2
  
  #If Player 2's guess is > the random number: Tells player(s) to guess lower; asks for Player 1's guess input.
  elif guess2 > n :
    prRed("Guess lower.")
    guess1 = int(input("Player 1, guess the correct number from 1-10: \n"))
    player2 = player2
  
  #If Player 2's guess is = the random number: Awards Player 2 with 1 pt; asks for Player 1's guess input.
  else :
    player2 = player2 + 1
    prGreen("\nScore: Player 1 = "+str(player1)+" pts | Player 2 = "+str(player2)+" pts\n")
    guess2 = 0
    n = randint(1,10)
    guess1 = int(input("Player 1, guess the correct number from 1-10: "))
  
  #If Player 1 gets 5 pts: Announces Player 1 as winner; ends game
  if player1 == 4 :
    prLightPurple("\nGAME OVER. Player 1 has 5 pts; Player 1 Wins!!")
    break
  
  #If Player 2 gets 5 pts: Announces Player 2 as winner; ends game
  elif player2 == 4 :
    prLightPurple("\nGAME OVER. Player 2 has 5 pts; Player 2 Wins!!")
    break
    