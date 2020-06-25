# notes 100 / 50 / 20 / 10 / 5 and 1
noteshun=0
notesfif=0
notestwe=0
notesten=0
notesfiv=0
notesone=0
total_amount = int(input("Please type the amount you want to withdraw:"))
while total_amount != 1 or total_amount!=0:
    if total_amount >= 100:
        noteshun = total_amount//100
        total_amount = total_amount % 100
    elif total_amount < 100 and total_amount >= 50:
        notesfif = total_amount//50
        total_amount = total_amount % 50
    elif total_amount < 50 and total_amount >= 20:
        notestwe = total_amount//20
        total_amount = total_amount % 20
    elif total_amount < 20 and total_amount >= 10:
        notesten = total_amount//10
        total_amount = total_amount % 10
    elif total_amount < 10 and total_amount >= 5:
        notesfiv = total_amount//5
        total_amount = total_amount % 5
    else:
        notesone = total_amount//1
        break

print("=-=-=-=-=-= BANKING =-=-=-=-=-=")
print("You will receive:")
print("{} Notes of 100".format(noteshun))
print("{} Notes of 50".format(notesfif))
print("{} Notes of 20".format(notestwe))
print("{} Notes of 10".format(notesten))
print("{} Notes of 5".format(notesfiv))
print("{} Notes of 1".format(notesone))
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
