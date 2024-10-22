def prYellow(skk): print("\033[93m {}\033[00m" .format(skk)) 
prYellow("This program is like a basic rock, paper, scissors game, but with a small twist. There are two more components added to this game: lizard and spock. This allows the game to have more varied results and less ties. Player one (you) will be asked what you want to choose. Once you type your answer, the code will randomly generate a move. It can either counter you, you counter them, or it ends in a draw (Rock crushes scissors and lizard, scissors cut paper and decapitate lizard, paper covers rock and disproves spock, lizard poisons spock and eats paper, and spock smashes scissors and vaporized rock).")

#imports the random integer function
from random import randint 
#defines the color-print
def prRed(skk): print("\033[91m {}\033[00m" .format(skk)) 
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk)) 
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk)) 
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk)) 
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk)) 
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk)) 

#This asks Player1 (you) what move they want to choose against the CPU. Their choices are listed in the question.
player1 =  input('Do you want to choose rock, paper, scissors, lizard, or spock?: ') 
#This allows the text answer to all turn lowercase, regardless of what you type in.
player1 = (str(player1)).lower() 
print("\nYou chose", player1 + ".")
#1=rock ; 2=paper ; 3=scissors ; 4=lizard ; 5=spock
player2 = randint(1,5) 
if player2 == 1:
  player2 = "rock"
elif player2 == 2:
  player2 = "paper"
elif player2 == 3:
  player2 = "scissors"
elif player2 == 4:
  player2 = "lizard"
elif player2 == 5:
  player2 = "spock"
print("The computer chose", player2 + ".")

#These conditional statements utilize nesting and logical operators to output the winner and the explanation.
if player1 == "rock" : 
  if player2 == "rock" :
    prLightPurple('\n'+"It's a draw! Rock can't crush rock.")
  elif player2 == "paper" :
    prLightPurple('\n'+"Computer wins! Paper covers rock.")
  elif player2 == "scissors" :
    prLightPurple('\n'+"You win! Rock crushes scissors.")
  elif player2 == "lizard" :
    prLightPurple('\n'+"You win! Rock crushes lizard.")
  elif player2 == "spock" :
    prLightPurple('\n'+"Computer wins! Spock vaporizes rock.")
if player1 == "paper" :
  if player2 == "rock" :
    prLightPurple('\n'+"You win! Paper covers rock.")
  elif player2 == "paper" :
    prLightPurple('\n'+"It's a draw! Paper can't cover/disprove paper.")
  elif player2 == "scissors" :
    prLightPurple('\n'+"Computer wins! Scissors cut paper.")
  elif player2 == "lizard" :
    prLightPurple('\n'+"Computer wins! Lizard eats paper.")
  elif player2 == "spock" :
    prLightPurple('\n'+"You win! Paper disproves spock.")
if player1 == "scissors" :
  if player2 == "rock" :
    prLightPurple('\n'+"Computer wins! Rock crushes scissors.")
  elif player2 == "paper" :
    prLightPurple('\n'+"You win! Scissors cut paper.")
  elif player2 == "scissors" :
    prLightPurple('\n'+"It's a draw! Scissors can't cut/decapitate scissors.")
  elif player2 == "lizard" :
    prLightPurple('\n'+"You win! Scissors decapitate lizard.")
  elif player2 == "spock" :
    prLightPurple('\n'+"Computer wins! Spock smashes scissors.")
if player1 == "lizard" :
  if player2 == "rock" :
    prLightPurple('\n'+"Computer wins! Rock crushes lizard.")
  elif player2 == "paper" :
    prLightPurple('\n'+"You win! Lizard eats paper.")
  elif player2 == "scissors" :
    prLightPurple('\n'+"Computer wins! Scissors decapitate lizard.")
  elif player2 == "lizard" :
    prLightPurple('\n'+"It's a draw!n Lizard can't eat/poison lizard.")
  elif player2 == "spock" :
    prLightPurple('\n'+"You win! Lizard poisons spock.")
elif player1 == "spock" and player2 == "rock" :
  prLightPurple('\n'+"You win! Spock vaporizes rock.")
elif player1 == "spock" and player2 == "paper" :
 prLightPurple('\n'+"Computer wins! Paper disproves spock.")
elif player1 == "spock" and player2 == "scissors" :
  prLightPurple('\n'+"You win! Spock smashes scissors.")
elif player1 == "spock" and player2 == "lizard" :
  prLightPurple('\n'+"Computer wins! Lizard poisons spock.")
elif player1 == "spock" and player2 == "spock" :
  prLightPurple('\n'+"It's a draw! Spock can't smash/vaporize spock.")
else:
  print('\n'+"If you misspelled your choice, please run the program again and input one of the five choices with the correct spelling!!")