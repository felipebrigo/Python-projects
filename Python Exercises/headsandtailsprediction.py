#Testing prediction in heads and tails using AI and self learning computing 
#Use random module to flip the coin (0-Heads and 1-Tails) and trying to discover the formula behind the scenes
def headsandtails():
    from random import randint
    flipcoin=randint(0,1)
    flipcoinlist.append(flipcoin)
    print(flipcoin)

def equilibrium():
    """This function suggest probability to bet in heads(0) or tails(1) depending on the historical data. 
    The main driver of this analysis is to maintaining the equivalent 50/50 - Equilibrium - for each side """
    probheads=probtails=0.00
    print (f'The probability to find heads (0) is {probheads} and tails (1) is {probtails}')


import pandas as pd
#addressfile=path()
#historicaldata=pd.read_csv(addressfile)
flipcoinlist=[]
answer="Y"
while answer=="Y" or answer=="y":
    headsandtails()
    answer=str(input("Do you want to continue? (Y/N):"))
    
print(flipcoinlist)
print("Thank you for playing our game")