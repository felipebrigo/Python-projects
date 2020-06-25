number = int(input("How many terms do you need to see?"))
count=2
fibonacci1=0
fibonacci2=1
fibonaccir=0
print('{} -> {} -> '.format(fibonacci1,fibonacci2), end="")
while count<number:
    fibonaccir=fibonacci1+fibonacci2
    print('{} -> '.format(fibonaccir), end="")
    fibonacci1=fibonacci2
    fibonacci2=fibonaccir
    count+=1