import math

a = float(input("Digite o tamanho do cateto adjacente: "))
b = float(input("Digite o tamanho do cateto oposto: "))
c = math.sqrt(a**2 + b**2)
print("A hipotenusa do triangulo vale {:.2f}".format(c))
