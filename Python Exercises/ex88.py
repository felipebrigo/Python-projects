# Lottery - 6 aleatory numbers from 1 to 60
from random import randint
games = int(input("Please how many games do you want?"))
n = n1 = count = 0
while count < games:
    suggestion = []
    numbersEachGames=0
    while numbersEachGames < 6:
        n = randint(1, 60)
        if n not in suggestion:
            suggestion.append(n)
            n1 = n
            numbersEachGames += 1
    count += 1
    suggestion=sorted(suggestion)
    print(suggestion)
