from time import sleep
from random import randint
import emoji

userchoice = 0
computerchoice=0
userscore=0
computerscore=0

def startgame():
    print("---------- ROCK / PAPER / SCISSORS ----------")
    print(emoji.emojize("To play ROCK please press 1 - :punch:", use_aliases=True))
    print(emoji.emojize("To play PAPER please press 2 - :raised_hand:", use_aliases=True))
    print(emoji.emojize("To play SCISSOR please press 3 - :scissors:", use_aliases=True))

def choiceanalysis():
    checkchoice = -1
    while checkcoice == -1:
        checkcoice = input("Please enter your choice number - 1 / 2 / 3: ")
        if (type(checkcoice) != int):
            print("Please re-type your choice. Only will be accepted numbers 1 for ROCK / 2 for PAPER or 3 for SCISSOR:")
            checkcoice = -1
        if checkchoice != 1 or checkchoice != 2 or checkchoice != 3:
            print("Please re-type your choice. Only will be accepted numbers 1 for ROCK / 2 for PAPER or 3 for SCISSOR :")
            checkcoice=-1
    return checkchoice
        
def choicetext():
    global userchoice    
    print("Let's play?")
    checkchoice=choiceanalysis()
    userchoice = checkchoice
    sleep(1.0)
    print(emoji.emojize("ROCK... :punch:", use_aliases=True))
    sleep(1.0)
    print(emoji.emojize("PAPER... :raised_hand:", use_aliases=True))
    sleep(1.0)
    print(emoji.emojize("SCISSOR... :scissors:", use_aliases=True))
    return userchoice

def computerrandomchoice():
    global computerchoice
    computerchoice=randint(1,3)
    return computerchoice

def item(chosen):
    if chosen == 1:
        selecteditem="ROCK"
    elif chosen == 2:
        selecteditem="PAPER"
    else:
        selecteditem="SCISSOR"
    return selecteditem

def whowon(userchoice, computerchoice):
        if userchoice == 1 and computerchoice == 1:
            won="DRAW"
        elif userchoice == 1 and computerchoice == 2:
            won="COMPUTER"
        elif userchoice == 1 and computerchoice == 3:
            won="YOU"
        elif userchoice == 2 and computerchoice == 1:
            won="YOU"
        elif userchoice == 2 and computerchoice == 2:
            won="DRAW"
        elif userchoice == 2 and computerchoice == 3:
            won="COMPUTER"
        elif userchoice == 3 and computerchoice == 1:
            won="COMPUTER"
        elif userchoice == 3 and computerchoice == 2:
            won="YOU"
        elif userchoice == 3 and computerchoice == 3:
            won="DRAW"
        return won

def points(won):
    if won == "YOU":
        userscore = userscore+1
    if won == "COMPUTER":
        computerscore = computerscore+1
    return userscore, computerscore

play="Y"

while play=="Y" or play=="y":
    startgame()
    choicetext()
    computerrandomchoice()
    won=whowon(userchoice, computerchoice)
    if won != "DRAW":
        points(won)
    usertext=item(userchoice)
    computertext = item(computerchoice)


    print("You played ", usertext, " and computer played ", computertext)

    print("... so  ", won, " won!")
    
    print("------- SCORES -------")
    print("USER POINTS: ", userscore)
    print("COMPUTER POINTS: ", computerscore)
    
    jogar=input("Play again? Y/N: ")
print("End of the game! See you soon...")