import string


def pig_latin_sentence(sentence: list):

    output = []

    for word in sentence.split():

        if word[-1] in string.punctuation:  # This way I handle punctuation
            punct = word[-1]
            word = word[-1]
        else:
            punct = ""

        if word.istitle():  # Keep the capitalized letter
            capital = True
            word = word.lower()
        else:
            capital = False

        vowels = set('aeiou')  # Use old solution here
        if word[0] in vowels:
            output.append(f"{word}-way")
        else:
            output.append(f"{word[1:]}-{word[0]}ay")

    return ' '.join(output)


test = pig_latin_sentence('this is a test translation')
print(test)
