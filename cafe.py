#pseudocode

menu = {"coffee", "croissant", "mocha", "capuccino"} # Create a list of 4 items for the menu.
stock = {"coffee": 100, "croissant": 30, "mocha": 50, "capuccino": 60} # These are the levels of stock for each item in the menu.
price = {"coffee": 3.5, "croissant": 2.8, "mocha": 4.5, "capuccino": 4} # This is the price for each item in the menu.

total_stock = sum(stock[item] * price[item] for item in menu) #  The calcul that give the total value of the stock
print(total_stock) # Print the total value of the stock


'''menu = {"coffee", "croissant", "mocha", "capuccino"}
stock = {"coffee": 100, "croissant": 30,"mocha": 50, "capuccino": 60}
price = {"coffee": 3.5, "croissant": 2.8, "mocha": 4.5, "capuccino": 4}
total_stock = int(stock[item] * price[item] for item in menu)
print(total_stock)'''

'''menu = {"coffee", "croissant", "mocha", "capuccino"}
stock = {"coffee": 100, "croissant": 30,"mocha": 50, "capuccino": 60}
price = {"coffee": 3.5, "croissant": 2.8, "mocha": 4.5, "capuccino": 4}
total_stock = int(stock(item) * price(item) for item in menu)
print(total_stock)'''

'''num_list = {'red car', 'green car', 'blue car', 'yellow car', 'silver car', 'gold car'}
sec_num_list = {'red car': 3, 'green car': 4, 'blue car': 5, 'yellow car': 6, 'silver car': 7, 'gold car': 8}
third_num_list = {'red car':3, 'green car':4, 'blue car': 5, 'yellow car': 6, 'silver car':7, 'gold car': 8}
new_num_list_ints = sum(sec_num_list[item] * third_num_list[item] for item in num_list)
print(new_num_list_ints)'''

'''num_list = {'1', '5', '8', '14', '25', '31'}
sec_num_list = {3, 4, 5, 6, 7, 8}
third_num_list = {3, 4, 5, 6, 7, 8}
new_num_list_ints = sum(sec_num_list[item] * third_num_list[item] for item in num_list)
print(new_num_list_ints)'''

'''num_list = ['1', '5', '8', '14', '25', '31']
sec_num_list = [3, 4, 5, 6, 7, 8]
third_num_list = [3, 4, 5, 6, 7, 8]
new_num_list_ints = [int( sec_num_list[item] * third_num_list[item] for item  in num_list)
print(new_num_list_ints)'''

'''num_list = ['1', '5', '8', '14', '25', '31']
print(num_list)

new_num_list_ints = [int(element) for element in num_list]
num_til_10 = list(range(0,10))
print(num_til_10)
print(new_num_list_ints)
print(sum(new_num_list_ints))'''

'''for num in num_til_10:
    print(num)

print("\n")'''