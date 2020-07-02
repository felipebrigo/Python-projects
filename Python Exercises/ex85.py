#Odds or Evens
odds_even=[]
n=1
for c in range (0,7):
    number=int(input("Please type number {}: ".format(n)))
    odds_even.append(number)
    n+=1
odds_even.sort()
odds=[]
even=[]
numbersorted=0
for c in range(0,7):
    if (odds_even[c]%2)==0:
       even.append(odds_even[c])
    elif (odds_even[c]%2)!=0:
        odds.append(odds_even[c])

print("The Even list is: {}".format(even))
print("The Odds list is: {}".format(odds))
    