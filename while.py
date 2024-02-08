# Pseudocode

total = 0
num = 0

user_number = int(input("Enter a number (-1 for exit): ")) # Ask user to enter a number.

while user_number != -1: # while loop that continues until the user enters -1.
    total += user_number# addition the sum of the number entered by the user.
    num += 1 # This section will count each time user input a number.
    user_number = int(input("Enter a number (-1 for exit): ")) # Ask user to enter another number.
    if user_number == -1: # This statement check if the user entered -1
        average = total / num # If -1 entered so then calculate the average.
        print(average) # Print the average.
        break # Exit the loop.



'''total = 0

user_number = int(input("Enter a number (-1 for exit): "))

while user_number != -1:
    total += user_number
    user_number = int(input("Enter a number (-1 for exit): "))
    if user_number == -1:
        average = total/user_number
        print(average)
        break'''

'''total = 0

user_number = int(input("Enter a number (-1 for exit): "))

while user_number != -1:
    total += user_number
    user_number = int(input("Enter a number (-1 for exit): "))
    if user_number == -1:
        print(total)
        break'''


'''i = 8

while i < 10:
   print(i)
   i = i + 1

sum1 = 0
i=0                  #initial even integer for the sum
while sum1 <= 10:
     sum1 += i
     i += 2
     print(sum1)'''


