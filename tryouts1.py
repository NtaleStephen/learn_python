# reversing a word
word = input("Enter a word: ")
reversed_word = word[::-1] 
# Why [::-1] works

# : means take whole string

# -1 means step backwards
print("Reversed word:", reversed_word)




# coutning the number of words in a sentence
sentence = input("Enter a sentence:     ").strip() # strip removes leading and trailing whitespace
# words = sentence.split() ---> split() by default splits on any whitespace and returns a list of words
words = sentence.split()
print("Number of words:", len(words))


# check if a word starts with a vowel

# Logic

# Make it lowercase for safety. Check first character. If it is in the set of vowels, then it starts with a vowel.

word = input("enter a word: ").lower()

if word.startswith(('a', 'e', 'i', 'o', 'u')):
    print("The word starts with a vowel.")
else:
    print("The word does not start with a vowel.")



# replacing a character in a sentence

sentence = input("Enter a sentence: ")
new_sentence = sentence.replace(" ", "_")  
# replace() takes two arguments: the substring to be replaced (in this case, a space " ") and the substring to replace it with (in this case, an underscore "_"). It returns a new string with all occurrences of the specified substring replaced.

print("New sentence:" , new_sentence)

# check if a strings contains only digits(without  int() 
text = input("Enter a string: ")

if text.isdigit():
    print("The string contains only digits.")
else:
    print("The string does not contain only digits.")
