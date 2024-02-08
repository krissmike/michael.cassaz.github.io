# pseudocode
# First of all i write variable for input "age"
# I declare all the statement
# 1st attempt I write all in the order from the task
"""
I wrote all in order from the task when I input a number up to 40 it only executed
"You're over the hill" so I will change the order of the statement.
"""
# I made in chronological order from youngest to oldest, and still have the same issue.
# 3rd attempt
"""
Elif for "65" and "100" can't be executed, so I will put them
before the statement "40".
"""
# Now everything work

age = int(input("Enter your age: "))

if age < 13:
    print("You qualify for the kiddie discount.")
elif age == 21:
    print("Congrats on your 21st!")
elif age >= 100:
    print("Sorry, you're dead.")
elif age >= 65:
    print("Enjoy your retirement!")
elif age >= 40:
    print("You're over the hill.")
else:
    print("Age is but a number.")
