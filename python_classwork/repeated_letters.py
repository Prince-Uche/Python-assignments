word = input("Input a word: ")

for letter in word:

    if letter in word:
        print("The word", word, "does not have any repetitive letters")

else:
    print(word.count(word))
