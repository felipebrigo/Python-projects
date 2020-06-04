from time import sleep
from random import randint
import emoji

userchoice = 0
computerchoice=0

def startgame():
    print("---------- ROCK / PAPER / SCISSORS ----------")
    print(emoji.emojize("To play ROCK please press 1 - :punch:", use_aliases=True))
    print(emoji.emojize("To play PAPER please press 2 - :raised_hand:", use_aliases=True))
    print(emoji.emojize("To play SCISSOR please press 3 - :scissors:", use_aliases=True))

def choiceanalysis():
    
    while (type(check_coice = input("Please enter your choice number - 1 / 2 / 3: ")) != int):
        print("Please re-type your choice. Only will be accepted numbers 1 for ROCK / 2 for PAPER or 3 for SCISSOR:")
    while (check_choice != 1) or (check_choice != 2) or (check_choice != 3):
        print("Please re-type your choice. Only will be accepted numbers 1 for ROCK / 2 for PAPER or 3 for SCISSOR :")
    return check_choice
        
def choicetext():
    global userchoice    
    print("Let's play?")
    choiceanalysis()
    userchoice= check_choice
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
        selectitem="TESOURA"
    return selectitem

def quemganhou(minhaescolha, computador):
        if minhaescolha == 1 and computador == 1:
            ganhador="EMPATE"
        elif minhaescolha == 1 and computador == 2:
            ganhador="COMPUTADOR"
        elif minhaescolha == 1 and computador == 3:
            ganhador="VOCÊ"
        elif minhaescolha == 2 and computador == 1:
            ganhador="VOCÊ"
        elif minhaescolha == 2 and computador == 2:
            ganhador="EMPATE"
        elif minhaescolha == 2 and computador == 3:
            ganhador="COMPUTADOR"
        elif minhaescolha == 3 and computador == 1:
            ganhador="COMPUTADOR"
        elif minhaescolha == 3 and computador == 2:
            ganhador="VOCÊ"
        elif minhaescolha == 3 and computador == 3:
            ganhador="EMPATE"
        return ganhador

jogar="S"

while play=="S" or play=="s":
    startgame()
    choicetext()
    computerchoice()
    ganhador=quemganhou(escolha, escolhacomputador)
    escolhatexto=item(escolha)
    escolhacomputadortexto = item(escolhacomputador)


    print("Você jogou ", escolhatexto, " e eu joguei ", escolhacomputadortexto)

    print("... portanto ", ganhador, "ganhou!")
    jogar=input("Jogar de novo? S/N: ")
print("Jogo terminado! Obrigado")