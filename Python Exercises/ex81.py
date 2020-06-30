ans = "Y"
number_list = []
while ans == "Y" or ans == "y":
    number = int(input("Please type one number:"))
    number_list.append(number)
    ans = input("Do you want to continue?[y/n]")
print("=-"*20)
print("You have typed {}".format(len(number_list)))
number_list.sort()
print(f'Your list ordered is:{number_list}')
for c, n in enumerate(number_list):
    print("Number {} at position {}".format(n, c))
