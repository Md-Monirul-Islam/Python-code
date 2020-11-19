def vowel(text):
    vowel = "aeiouAEIOU"
    print(len([letter for letter in text if letter in vowel]))
    print([letter for letter in text if letter in vowel])
vowel("Munna")