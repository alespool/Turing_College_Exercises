# most efficient way
from heapq import merge
print(list(merge(a,b,c)))

it = merge(a,b,c)
print(next(it))
print(next(it))

from itertools import islice
print(list(islice('abcdefghi', 2, 4)))
print(list(islice('abcdefghi', None, 2)))


# it doesnt have to eat all the values in the way in
# a generator runs on command
# if the list is very long it will get out only the stuff we need
print(list(islice(it, 3)))

import random

import bisect
cuts = [60,70,80,90]

grades = 'FDCBA'

print(grades[bisect.bisect(cuts, 76)])

try_bisect = [grades[bisect.bisect(cuts, score)] for score in [76, 92, 80, 70, 69, 91, 99, 100]]
print(try_bisect)

# bisect is mainly used for searching ranges
print(sorted([10,30,5] + [1,4,22]))

a = [1, 11, 25]
b = [5, 10, 20]
c = [2, 15, 21]

#this not very efficient as they get larger
print(sorted(a+b+c))




