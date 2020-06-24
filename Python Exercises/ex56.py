import numpy as np
dados=[]

def printresult():
    pessoa=1
    for pessoa in range (1,5):
        print("----- {} ª Pessoa -----".format(pessoa))
        inputpessoa()
        pessoa=+1
        
def inputpessoa():
    #nome=str(input("Digite o nome:"))
    idade=int(input("Digite a idade:"))
    sexo=str(input("Digite o sexo:"))
    dados.append([idade,sexo])
    return dados

def answer():
    matriz=np.array(dados)
    matrizidade=matriz[ : ,0]
    matrizidadeajustada=list(map(int,matrizidade))
    print(matrizidade)
    print("A média de idade do Grupo é: {}")

printresult() 
answer()