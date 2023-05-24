print(sum([0.1] * 10))

from math import fsum

print(fsum([0.1] * 10))
print(fsum([0.1] * 10) == 1.0)

# Default Dictionaries
from collections import defaultdict

d = {'raymond': 'red'}
e = defaultdict(lambda: 'black')
e['raymond'] = 'red'

print(d)
print(e)

print(e['rachel'])
# default dict is same as regular dict, but when key is missing
# it runs a factory function and whatever it returns is inserted
# into the dictionary


print("Let's see the defaultdict grouping with sets")

# a common usecase for defaultdict is for grouping
d = defaultdict(set)
d['t'].add('tom')
d['m'].add('mary')
d['t'].add('tim')
d['t'].add('tom')
d['m'].add('martin')

# Default dict creates a new container to store elements with a
# common feature

from pprint import pprint

pprint(d, width=40)

print("Let's see the defaultdict grouping with lists")
# also using default dict with list for grouping
d = defaultdict(list)
d['t'].append('tom')
d['m'].append('mary')
d['t'].append('tim')
d['t'].append('tom')
pprint(d, width=40)

d = defaultdict(list)
names = '''david betty susan mary darlene sandy davin shelly becky beatrice tom michael wallace'''.split()
print(names)

for name in names:
    feature = len(name)
    d[feature].append(name)

pprint(d, width=40)

# Key Functions
# Commonly used in sorting, smallest, largest, minimum, hip-q,
# it takes one argument and transforms it into a key

pprint(sorted(names, key=len))

# Tkaes one of the elements and computes a key for each

# use the key functions with zip

list(zip('abcdef', 'ghijklm'))
# [('a', 'g'), ('b', 'h'), ('c', 'i'), ('d', 'j'), ('e', 'k'), ('f', 'l')]

from itertools import zip_longest

list(zip_longest('abcdef', 'ghijklm'))
# [('a', 'g'), ('b', 'h'), ('c', 'i'), ('d', 'j'), ('e', 'k'), ('f', 'l'), (None, 'm')]

list(zip_longest('abcdef', 'ghijklm', fillvalue='x'))
# [('a', 'g'), ('b', 'h'), ('c', 'i'), ('d', 'j'), ('e', 'k'), ('f', 'l'), ('x', 'm')]

print('*' * 100)

m = [
    [10, 20],
    [30, 40],
    [50, 60],
]
print(m)

print(list(zip([10,20],[30,40],[50,60])))
# [(10, 30, 50), (20, 40, 60)]

pprint(list(zip(*m)),width = 15)
# [(10, 30, 50),
#  (20, 40, 60)]

# zip(*) is useful for inverting/transposing matrices and also other multi-dimensional data

for row in m:
    print(row)

# [10, 20]
# [30, 40]
# [50, 60]

for row in m:
    for col in row:
        print(col)

# 50
# 10
# 20
# 30
# 40
# 60

# There 's 2 loops inside the list comprehension  you can use to flatten a 2-d data structure
flatten_m = [x for row in m for x in row]
# [10, 20, 30, 40, 50, 60]

# when we have an iterator, we can just list(iterator) to make them a list
it = iter('abcd')
print(it)
print(list(it))
# ['a', 'b', 'c', 'd']


