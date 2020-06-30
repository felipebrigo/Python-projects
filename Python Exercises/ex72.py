counting = ("zero", "one", "two", "three", "four", "five",
            "six", "seven", "eight", "nine", "ten")
number = int(input("Please type a number from 0 to 10:"))
while number < 0 or number > 10:
    number = int(input("Please re-type a number from 0 to 10:"))
print("You typed the number {}".format(counting[number]))