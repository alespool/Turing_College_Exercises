from collections import defaultdict
from pprint import pprint

d = defaultdict(list)
d['Raymond'].append('red')
d['Rachel'].append('blue')
d['Matthew'].append('blue')

d['Raymond'].append('MAC')
d['Rachel'].append('PC')
d['Matthew'].append('VTech')

# it is normal to use a default dict to accumulate data
# and then convert to dict
# defaultdict can be used for grouping and data accumulation
# pprint(dict(d))

# invert or reverse one-to-many mappings with defautldict
# Model one-to-many: dict(one, list_of_many)

e2s = {
    'one': ['uno'],
    'two': ['dos'],
    'three': ['tres'],
    'trio': ['tres'],
    'free': ['libre', 'gratis'],
}

# pprint(e2s)

# Need to loop over each word to make them one to one
s2e = defaultdict(list)

for eng_words, span_words in e2s.items():
    for span in span_words:
        s2e[span].append(eng_words)

pprint(s2e)

# Put the ones as a key, adn the many as a list and convert them by looping over them
# and using a defaultdict mapped to a list

# what if theres a one-to-one relation?

e2s = {
    'one': 'uno',
    'two': 'dos',
    'three': 'tres'
}

pprint(e2s)
# use dictionary comprehension for inverted bijection (one-to-one)
s2e = {span: eng for eng, span in e2s.items()}
pprint(s2e)