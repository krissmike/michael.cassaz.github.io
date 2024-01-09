# pseudocode
# write a loop with a range


n = 5  # number of row
stars = "*" # this the pattern that I want to display
for i in range(1,2 * n):  # In the bracket I declare for each row to display up to 5 which is "n"
     if i <= n: # if the range is less than "n" or equal
        print(stars * i) # the result will be display on "*"
     else: # the range is greater than 5
        print(stars * (2 * n - i)) # it will display another set of the range but decreased. "- i" allow to decrease

'''stars = "*"
for i in range(0 ,10):
                print(stars)'''



'''
for x in range(1, 6):
    for y in range(1, 6):
        print('{} * {} = {}'.format(x, y, x * y))
    print("")
    '''
'''print("*Printing even numbers in a range*")
range_num = int(input("Enter the upper bound of the range (max number you'd like to go up to): \n"))

for i in range (0, range_num):   #  We define a for loop that runs from 0 to the entered number. i is the current number that the loop is on.
	if i % 2 == 0: # This checks if the current number of the loop is EVEN. (i.e. if you divide it by 2, you get a 0 remainder. This is what the %, or MODULUS, operator does.)
		print(i)
        '''

'''given_number = int(input("Enter a number: \n"))

if given_number % 2 == 0:  # If number is even.
    stars = "*"
    for i in range(0, 10):
        print(stars)
        stars = stars + "*"

elif (given_number % 2 != 0):  # If number is odd, i.e. the number divided by 2 does NOT have a remainder of 0.
    stars = "**********"
    for i in range(0, 10):
        index = 10 - i  # i goes from 0 to 10 in this loop
        print(stars[0:index])'''


'''for i in range (1,10):
        if i > 5:
                print(i)'''

'''for x in range(1, 6):
    for y in range(1, 6):
        print('{} * {} = {}'.format(x, y, x * y))
    print("")'''

