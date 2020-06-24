print("-=-=-=-=-=-= Arithmetic Progression =-=-=-=-=-=-")
start = int(input("Please type starting number:"))
constant = int(input("Please type the constant of your AP:"))
counting = 10
number = []
number = [start]
n = 1
qtdenumbers = 10


def ap(counting):
    global n
    global start
    while n < counting:
        newstart = start+constant
        number.append(newstart)
        start = newstart
        n += 1
    n = 0
    while n < counting:
        print('{} -> '.format(number[n]), end='')
        n += 1
    print("PAUSA")

while counting != 0:
    ap(counting)
    counting = int(input("QUANTOS TERMOS VOCÊ GOSTARIA DE VER A MAIS?"))
    qtdenumbers = qtdenumbers+counting

print("PROGRESSÃO FINALIZADA COM {} TERMOS MOSTRADOS".format(qtdenumbers))
