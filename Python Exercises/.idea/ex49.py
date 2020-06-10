num=int(input("Por favor, digite um número para saber sua tabuada:"))
for n in range(1,11):
    print('{:2} x {:1} = {}'.format(n,num,(n*num)))