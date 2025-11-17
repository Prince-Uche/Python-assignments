letter = str(input("Enter a letter: "))

vowel = ("a", "e", "i", "o", "u")

consonant = ("b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z")

if (letter in vowel):
    print('\'',letter,"\'", "is a vowel")

elif (letter in consonant):
    print('\'',letter,"\'", "is a consonant")

else:
    print("Invalid option. Try again!")
