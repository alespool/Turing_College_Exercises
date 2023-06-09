import glob
import os
import csv

folder_path = '/Sprint 1/congress_data'

# A global wildcard expansion
# glob.glob('*.txt')

# open a file that has an encoding
# with open(f'{folder_path}/congress_votes_114-2016_s20.csv', encoding='utf-8') as f:
    # print(f.read())

# use next or islice to remov elements from an iterator
# it = iter('abcdefg')
# print(next(it))
# print(next(it))
# #it pritns only from c as the others ahve been already removed and iterated through
# print(list(it))

with open(f'{folder_path}/congress_votes_114-2016_s20.csv', encoding='utf-8') as f:
    for row in csv.reader(f):
        print(row)

# tuple packing and unpacking
t = ('Raymond', 'Hettinger', 54, 'python@crm.com')
print(type(t))

print(len(t))

# Unpacking it
fname, lname, age, email = t

names = 'Raymond  Rachel Matthew'.split()
colors = 'red blue yellow'.split()
cities = 'austin dallas austin houston chicago dallas austin'.split()

# logo idioms
# for i in range(len(names)):
#     print(names[i].upper())

# for name in names:
#     print(name.upper())

for i in range(len(names)):
    print(i+1, names[i])
# You can choose the start
for i, name in enumerate(names, start = 1):
    print(i, name)

# reversing the looping idioms
for color in reversed(colors):
    print(color)

# bring thee names together with the colors pair wise
n = min(len(names), len(colors))
# one way, nto the best
# for i in range(n):
#     print(names[i], colors [i])

# best way using zip
for name, color in zip(names, colors):
    print(name, color)

print('*' * 100)
# show all colors in alphabetical order

for color in sorted(colors):
    print(color)
print('*' * 100)

# sort colors by length
for city in reversed(sorted(set(cities))):
    print(city)

# pretty cool but long
for i,city in enumerate(map(str.upper, reversed(sorted(set(cities))))):
    print(i, city)

import collections
c = collections.Counter()
c['red'] += 1
print(c)
# Counter({'red': 1})
c['blue'] += 1
print(c)
# Counter({'red': 1, 'blue': 1})
c['red'] += 1
print(c)
# Counter({'red': 2, 'blue': 1})
print(c.most_common(1))
# [('red', 2)]
print(list(c.elements()))
# ['red', 'red', 'blue']


# assertions are used for checkpointing parts we believe to be true
assert 5 + 3 == 8
assert 5 + 3 == 10
