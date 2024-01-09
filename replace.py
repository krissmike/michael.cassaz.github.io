#pseudocode

word = "The!quick!brown!fox!jumps!over!the!lazy!dog." # 1st I declare the variable with the sentence
word_replace = word.replace("!", " ") # variable replace and inside the parentheses the symbol that I want to replace.
# Inside the parentheses, the 1st symbol is what I want to change, and the 2nd symbol is what I want to change it to.
print(word_replace)

upper_word = word_replace.upper()
print(upper_word)
# I can keep the variable 'word_replace' as it already has the space, but I just need to add '.upper()'
lower_word = upper_word.lower()
print(lower_word)
# I just need to add the function '.lower()' to the previous variable.