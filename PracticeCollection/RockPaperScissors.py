#Below is a very simple program for the classic Rock, Paper, Scissors game, utilizing conditional statements for all cases.
#It accepts a string input for two players, and returns a string statement telling who wins based on the inputs.

from random import randint

def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))

player2 = randint(1,3)

player1 = input('Player 1, do you want to be rock, paper, or scissors?: ')

def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
if player1 == "rock" and player2 == int(1):
  prLightPurple('\n'+"It's a draw!")
elif player1 == "rock" and player2 == int(2):
  prLightPurple('\n'+"Player 2 wins!")
elif player1 == "rock" and player2 == int(3):
  prLightPurple('\n'+"Player 1 wins!")
elif player1 == "paper" and player2 == int(1):
  prLightPurple('\n'+"Player 1 wins!")
elif player1 == "paper" and player2 == int(2):
  prLightPurple('\n'+"It's a draw!")
elif player1 == "paper" and player2 == int(3):
  prLightPurple('\n'+"Player 2 wins!")
elif player1 == "scissors" and player2 == int(1):
  prLightPurple('\n'+"Player 2 wins!")
elif player1 == "scissors" and player2 == int(2):
 prLightPurple('\n'+"Player 1 wins!")
elif player1 == "scissors" and player2 == int(3):
  prLightPurple('\n'+"It's a draw!")
else:
  prLightPurple('\n'+"Something is mispelled!!")