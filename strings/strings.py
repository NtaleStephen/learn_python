text = input("Enter a sentence: ").strip()

print("Lowercase: ", text.lower())
print("word count: ", len(text.split()))
print("Number of 'a'; ", text.lower().count("a"))