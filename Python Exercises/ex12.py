valor = float(input("Qual é o valor do produto? R$"))
desconto = float(input("Qual é o percentual de desconto?"))
novovalor = valor * (1-(desconto/100))
print("O valor do produto, que originalmente era de R${}, depois de aplicar o desconto, passou a ser de R${}".format(valor, novovalor))