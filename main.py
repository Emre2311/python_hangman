import sys
from random import randint
def Home():
    inp = input("Do you want to play a game? (y/n)")
    if inp == 'y':
        print("Let's go!")
    elif inp == 'n':
        sys.exit()
    else:
        print('Please input y or n.')
        Home()

Home()

person = input("What's your name?")  #this is for the main menu

def player_info(name):
    print("Hello " + name + "!")
player_info(person)

def maine():
    print("What would you like to do?")
    menu_action = input("play games, info, quit:")
    if menu_action == "play games":
        print("...starting game system...")
    elif menu_action == "info":
        print("These games were made by  Emre  They are the first games I have created, and I hope you enjoy!")
        maine()
    elif menu_action == "quit":
        sys.exit()
    else:
        print("Please select play games, info, or quit")
        maine()

def hang_man():
    words = ['word','swamp', 'keyboard', 'slammed', 'mortal', 'columbine', 'dictionary', 'theory', 'post', 'desktop',       
    'fan', 'digits', 'collab', 'sign', 'adjective', 'polar', 'knight', 'propeller', 'quadratic', 'quarantine'] 
    word = words[randint(0,19)]
    print('The word is '+str(len(word))+' letters long.')
  
    length = len(word)
    guess = []
    incorrect = 0
    guesses = length + 3
    while incorrect < guesses:
        if guess == list(word):
            resta = input("you win! Would you like to play again? (yes/no)")
            if resta == 'yes':
                hang_man()
            elif resta == 'no':
              game_menu()
            else: 
              game_menu()
        letter = input('please input a letter:')
        if letter in word:
            guess.append(letter)
            print("that letter is in the word! you have " + str(guesses - incorrect) + " incorrect guesses left.")
            print("you have these letters correct: " + str(guess))
        elif letter not in word:
            incorrect += 1
            print("that letter is not in the word. You have " + str(guesses - incorrect) + " incorrect guesses left")
        else:
            print("dont cheat.")
            incorrect += 1
    repla = input('You lost! The word was '+word+'. Would you like to play again? (yes/no)')
    if repla == 'yes':
      hang_man()
    else:
      game_menu()
maine()

def r_p_s():
    t = ["Rock", "Paper", "Scissors"]
    computer = t[randint(0,2)]
    player = False
    while player == False:
        player = input("Rock, Paper, Scissors, or Quit?")
        if player == computer:
            print("Tie!")
        elif player == "Rock":
            if computer == "Paper":
                print("You lose!", computer, "covers", player)
            else:
                print("You win!", player, "smashes", computer)
        elif player == "Paper":
            if computer == "Scissors":
                print("You lose!", computer, "cut", player)
            else:
                print("You win!", player, "covers", computer)
        elif player == "Scissors":
            if computer == "Rock":
                print("You lose!", computer, "smashes", player)
            else:
                print("You win!", player, "cuts", computer)
        elif player == "Quit":
            game_menu()
        else:
            print("That is not a valid play. Check your spelling!")
        player = False
        computer = t[randint(0,2)]

def game_menu():
    print("What game would you like to play?")
    game = input("RPS, Hangman, (others coming soon!)")
    if game == "RPS":
        print("...starting RPS...")
        r_p_s()
    elif game == "Hangman":
        print("...starting Hangman...")
        hang_man()
    else:
        print('please select a game.')
        game_menu()
game_menu()
