# Pseudocode

sentence = input("Enter a sentence: ") # Ask the user to enter a sentence.
while not sentence: # If the user doesn't enter a sentence the loop will not be executed, and the user has to re-enter the sentence.
    print("You haven't entered anything. Please enter a sentence.")
    sentence = input("Enter a sentence: ")
last_sentence = "" # Here we create an empty string for store the result.

for index in range(len(sentence)): # In this part we create the loop with a statement.
    if index % 2 == 1:  # Check if the index is an odd or even number.
        last_sentence += sentence[index].lower() # If the result is an odd number then it convert in lower to the chain of the sentence.
    else:
        last_sentence += sentence[index].upper() # If the result is an odd number then it convert in upper to the chain of the sentence.

print(last_sentence) # Here it prints the result with the modifications.


final_sentence = "" # Here we create an empty string for store the result.
new_sentence_split = sentence.split() # Here we create a variable for split the sentence.


for index in range(len(new_sentence_split)): # In this part we create the loop with a statement.
    if index % 2 == 0: # Check if the index is an odd or even number.

        final_sentence += new_sentence_split[index].lower() + " " # If the result is an odd number then it convert in lower to the chain of the sentence plus add a space.
    else:

        final_sentence += new_sentence_split[index].upper() + " " # If the result is an odd number then it convert in upper to the chain of the sentence plus add a space.

print(final_sentence)  #Here it prints the result with the modifications.




'''original_string = "Hello world!"
new_string = original_string[0:5]
print(new_string)'''
'''print("Hello \n\"bob\"") # the "\n" this code make a new line to the text in the output
print("The escape sequence \ncreates a new line in a print statement")'''

'''name = "Peter"
print("Hello, {}!".format(name))

name = "Peter"
print(f"Hello, {name}!") # this the same syntax above just in version more recent '''

'''number_builder = ""
i = 0
while i <= 50:
    if i % 2 == 0:
        number_builder += str(i) + " "
    i += 1
print(number_builder)'''

'''number_builder = [] #note the variable has to be a list rather than a string
i = 0
while i <= 50:
    if i % 2 == 0:
        number_builder.append(str(i))
    i += 1
print(" ".join(number_builder))'''

'''string = 'Hello world!'
fizz = string[0:5]
print(fizz)'''

'''print("Example 2: ")

fact1 = "The original name of Windows was Interface Manager."
fact1 = fact1.upper()
print(fact1)
fact1 = fact1.lower()
print(fact1)'''

'''print("Example 3: ")

sentence = "ThisHELLOisHELLOrandomHELLOtextHELLOweHELLOareHELLOgoingHELLOtoHELLOsplitHELLOapart"
split_sentence = sentence.split("HELLO")
print(split_sentence)'''

'''print("Example 4: ")

fact2 = "          The$first$electronic$computer$ENIAC$weighed$more$than$27$tons.          "
fact2 = fact2.replace("$", "WOW!")
print(fact2)
fact2 = fact2.strip()
print(fact2)
fact2 = fact2.split("WOW!")
print(fact2)'''

