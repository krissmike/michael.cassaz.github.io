# Pseudocode
# I will start to write my first while loop

total = 0

user_number = int(input("Enter a number (-1 for exit): "))

while user_number != -1:
    total += user_number
    user_number = int(input("Enter a number (-1 for exit): "))
    if user_number == -1:
        print(total)
        break




