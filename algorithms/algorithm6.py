# how many times each letter apears in a word

word = "banana"

letter_count = {}

for letter in word:
    if letter in letter_count:
        letter_count[letter] += 1
    else:
        letter_count[letter] =1

print(letter_count)