from time import sleep
from random import randint
import emoji

escolha = 0
escolhacomputador=0

def startgame():
    print("---------- PEDRA / PAPEL / TESOURA ----------")
    print(emoji.emojize("Para jogar PEDRA digite 1 - :punch:", use_aliases=True))
    print(emoji.emojize("Para jogar PAPEL digite 2 - :raised_hand:", use_aliases=True))
    print(emoji.emojize("Para jogar TESOURA digite 3 - :scissors:", use_aliases=True))

def choicetext():
    global escolha    
    print("Vamos Jogar?")
    escolha = input("Digite sua opção:")
    if (escolha != 1) or (escolha != 2) or (escolha != 3):
        print("Por favor, digite um número válido - 1 / 2 / 3:")
                
    print(type(escolha))
    while type(escolha) != int:
        print("Caractere Inválido!")
        escolha = int(input("Digite sua opção - 1 / 2 / 3:"))
    
    while not escolha in range(1,4):
        print("Número Inválido!")
        escolha = int(input("Digite sua opção:"))

    sleep(1.0)
    print("PEDRA...")
    sleep(1.0)
    print("PAPEL...")
    sleep(1.0)
    print("TESOURA...")
    return escolha

def computerchoice():
    global escolhacomputador
    escolhacomputador=randint(1,3)
    return escolhacomputador

def item(escolhido):
    if escolhido == 1:
        selectitem="PEDRA"
    elif escolhido == 2:
        selectitem="PAPEL"
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

while jogar=="S" or jogar=="s":
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