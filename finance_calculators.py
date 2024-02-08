import math
#pseudocode

#Capstone project
# I will create a project for a  small financial company

# These 2 codes we will display the information about "investment" and "bond"
print("Investment - to calculate the amount of interest you'll earn on your investment")
print("Bond - to calculate the amount you'll have to pay on a home loan")

# User enter "investment" or "bond"/ ".lower()" allow to write in upper or lower
user_select = input("Select your choice ( Investment or Bond): ").lower()

# This is a statement, so if user enter "investment"
if user_select == "investment":
    # User enter the amount of money
    amount_money = int(input("Enter the amount of money for your deposit: "))
    # User enter the interest rate only numbers(decimal include), no symbol %
    interest_rate = float(input("Enter your interest rate wish (only numbers): ")) / 100
    # User enter how many years
    years = int(input("How many years: "))
    # User choice simple or compound / .lower() allow to write in upper or lower
    interest_type = input("Select the type of interest (Simple or Compound): ").lower()
    # A new statement after select "simple"
    if interest_type == "simple":
        # This is the calculation for find the total amount
        total_amount = amount_money * (1 + interest_rate * years)
        print("Total amount is", total_amount)
    # A new statement after select "simple"
    elif interest_type == "compound":
        # This is the calculation for find the total amount
        total_amount = amount_money * math.pow((1 + interest_rate),years)
        print("Total amount is", total_amount)
# Here this is a statement, so if user enter "Bond"
elif user_select == "bond":
    # User enter the value of the house
    value_house = int(input("Enter the value of the house: "))
    # User enter the interest rate, only numbers(decimal include), no symbol %
    interest_rate = float(input("Enter your interest rate wish (only numbers): ")) / 100 / 12
    # User enter how many month
    month = int(input("How many months: "))
    # This is the calculation for find the total amount to be refund
    repayment = (interest_rate * value_house)/(1 - (1 + interest_rate)**(-month))
    # This is for display the total amount to refund
    print("Total amount to refund: ", repayment)
# If the user's choice is not investment or bond, the else will be executed
else:
    print("Select between Investement or Bond")


