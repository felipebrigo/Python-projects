exp = str(input("Please type your expression:"))
count = []
total = 0
for carac in exp:
    if carac == "(":
        count.append(1)
    elif carac == ")":
        count.append(-1)
if count[0] == -1 or len(count) == 0:
    print("Your expression has some problem!")
    total = -1
total = sum(count)+total
if total != 0:
    print("Your expression has some problem!")
elif total == 0:
    print("Your expression is OK!")