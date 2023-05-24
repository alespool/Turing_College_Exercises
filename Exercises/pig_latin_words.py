import string

def pig_latin(word: str):

    if word[-1] in string.punctuation: # This way I handle punctuation
        punct = word[-1]
        word = word[-1]
    else:
        punct = ""

    if word.istitle():      # Keep the capitalized letter
        capital = True
        word = word.lower()
    else:
        capital = False

    vowels = set('aeiou')       # Check for two different vowels
    if len(vowels.intersection(word)) < 2:
        final_word = word[0]
        prefix = 'ay'
    else:
        final_word = ""
        prefix = "way"

    return (word[1:].capitalize() if capital else word[1:]) + final_word + prefix + punct



    # Old simple solution
    # if word[0] in vowels:
    #     return word[1:] + "-way"
    # else:
    #     return f"{word[1:]}-{word[0]}ay"


test = pig_latin("Python")
print(test)
test = pig_latin("Earnest")
print(test)

# Another solid solution from book authors

def pig_latin(word):
    if word[0] in 'aeiou':
        return f'{word}way'

    return f'{word[1:]}{word[0]}ay'


print(pig_latin('python'))