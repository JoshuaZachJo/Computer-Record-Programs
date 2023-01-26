while True:
    string = input("Enter a string: ")
    vowels = "aeiouAEIOU"
    consts = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    lower = "abcdefghijklmnopqrstuvwhyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letters = vowel = consonant = uppercase = lowercase = 0
    for i in string:
        if i in lower or i in upper:
            letters = letters + 1
        if i in vowels:
            vowel = vowel + 1
        elif i == " ":
            pass
        else:
            consonant = consonant + 1
        if i.isupper():
            uppercase = uppercase + 1
        if i.islower():
            lowercase = lowercase + 1
    print("Total number of letters: ", letters)
    print("Total number of vowels: ", vowel)
    print("Total number of consonants: ", consonant)
    print("Total number of uppercase letters: ", uppercase)
    print("Total number of lowercase letters: ", lowercase)
