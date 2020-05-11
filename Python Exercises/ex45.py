from time import sleep
from random import randint

def startgame():
    print("---------- PEDRA / PAPEL / TESOURA ----------")
    print("Para jogar PEDRA digite 1")
    print("Para jogar PAPEL digite 2")
    print("Para jogar TESOURA digite 3")

def choicetext():
    print("Vamos Jogar?")
    escolha = int(input(print("Digite sua opção:")))
    while escolha < 1 or escolha > 3:
        print("Número Inválido!")
        escolha=int(input(print("Digite sua opção:")))

    sleep(1.0)
    print("PEDRA...")
    sleep(1.0)
    print("PAPEL...")
    sleep(1.0)
    print("TESOURA...")
    return escolha

def computerchoice():
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
    escolha=item(escolha)
    escolhacomputador = item(escolhacomputador)


    print("Você jogou ", escolha, " e eu joguei ", escolhacomputador)

    print("... portanto ", ganhador, "ganhou!")
    jogar=input(print("Jogar de novo? S/N: "))
print("Jogo terminado! Obrigado")