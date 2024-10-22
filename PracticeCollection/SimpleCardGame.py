#Defined functions are called to a particular color for print statements 
# #source: https://www.geeksforgeeks.org/print-colors-python-terminal/
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prCyan(skk): input("\033[96m {}\033[00m" .format(skk)) 

#random module is imported for more efficient calls for random functions.
import random 

#Variable for points is referenced. Each player starts off with 0 pts.
player1_pts = 0 
player2_pts = 0

prLightPurple("Welcome to the Card Game 'War' !!! In this game, the user (Player 1) will be playing against the automated bot opponent (Player 2). ")
prPurple("The Dealing: The deck is divided evenly. Each player receives 26 cards. Each player picks a card at the same time and the player with the higher card value wins the round and receives a point. If the card values are the same, no points will be awarded.")
prRed("The Game ends when a player first has 10 points.\n") 

def play():
  #Since a variable was declared outside of the specific function, the outer scope variable is declared global.
  global player1_pts 
  global player2_pts

#user inputs 'enter' button to start each round.
  p = input("\nPress [ENTER] to play: \n") 
  if p == "":
    #Lists are created to house card values
    player1_cards = [] 
    player2_cards = []

    #Lists of suits is created
    suits = ["◆", "♥", "♠", "♣"] 

    #Random integer from 1-13 is selected to determine card face value for both player cards.
    n1 = random.randint(1,13) 
    n2 = random.randint(1,13)

    #Random suit is selected from list of suits for each player.
    s1 = random.choice(suits) 
    s2 = random.choice(suits)

    #Value of card face is appended into player cards list.   
    player1_cards.append(n1) 
    player2_cards.append(n2)

    #Conditional statements: If a value is <,>,= to other player card value, 
    # then a specific action is performed, such as awarding a player 1 pts or 0 pts.
    if int(n1) > int(n2): 
      player1_pts = 1 + player1_pts
    elif int(n1) < int(n2):
      player2_pts = 1 + player2_pts
    elif int(n1) == int(n2):
      player2_pts = 0 + player2_pts
  
    #The selected card of each player is outputted: Value of card + suit.
    print("Player 1 Card:", player1_cards, s1) 
    print("Player 2 Card:", player2_cards, s2)

    #The amount of pts each player has is outputted.
    print("Player 1: ", player1_pts, "points") 
    print("Player 2: ", player2_pts, "points")
    
    #Conditional statement: If a certain player has 10 pts first, that player wins. 
    # If none of these conditions are met (else), then the function 'play()' is run again.
    if player1_pts == 10: 
      prGreen("Player 1 wins!")
    elif player2_pts == 10:
      prGreen("Player 2 wins!")
    else:
      play()

#Calls function play to begin game program
play() 