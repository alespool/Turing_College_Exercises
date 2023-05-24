vowels = ['a', 'e', 'i', 'o', 'u']


def pig_latin(word: str):
    word = word.lower()
    if word[0] in vowels:
        return word[1:] + "-way"
    else:
        final_word = word[0]
        return word[1:] + final_word + "-ay"


test = pig_latin("Python")
print(test)
test = pig_latin("Earnest")
print(test)

