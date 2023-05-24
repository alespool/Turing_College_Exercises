from pprint import pprint
from math import fsum, sqrt
from typing import *
from collections import defaultdict
from functools import partial


Point = Tuple[int, ...]

points = [
    (10,41,23),
    (22,30,29),
    (11,42,5),
    (20,32,4),
    (12,40,12),
    (21,36,23),
]

pprint(points)


def mean(data: Iterable[float]) -> float:
    """Accurate arithmetic mean"""
    data = list(data)
    return fsum(data) / len(data)


print(mean([8,2,4]))


def dist(p: Point, q: Point, fsum=fsum, sqrt=sqrt, zip=zip):
    """Euclidean distance function for multi-dimensional data"""
    return sqrt(sum([(x - y) **2  for x, y in zip(p,q)]))


def assign_data(centroids, data):
    d = defaultdict(list)
    for point in data:
        closest_centroid = min(centroids, key = partial(dist, point))
        d[closest_centroid].append(point)
    return d


def compute_centroids(groups):
    """Compute the centroid of each group"""
    return [tuple(map(mean, zip(*group))) for group in groups]


# How to find minimum centroid?
centroids = [(9, 39, 20), (12, 36, 25)]
point = (11,42, 5)
result = min([dist(point, centroid) for centroid in centroids])
print(f'The minimum distance from the closest centroid is: {result}')

# To get the specific centroid, we use key functions to get values
result = min(centroids, key = lambda centroid: dist(point, centroid))
print(f'The closest centroid from the point {point} is: {result}')

# a better way of doing this lamba/min thing is to use partial
pow(2, 5)
twopow = partial(pow, 2)
print(twopow(5))
# Checking
print(min(centroids, key = partial(dist, point)))

# Testing if main function works
# pprint(assign_data(centroids, points) , width = 45)

groups = [
    [(10, 41, 23),
                   (11, 42, 5),
                   (20, 32, 4),
                   (12, 40, 12)],
    [(22, 30, 29),
                    (21, 36, 23)]
]

pprint(groups)

group = [(10, 41, 23), (11, 42, 5), (20, 32, 4), (12, 40, 12)]
one_group = tuple(map(mean, zip(*group)))
result = [tuple(map(mean, zip(*group))) for group in groups]
pprint(one_group)
pprint(result)




# # Just easy check
# for point in points:
#     print(point, dist(point, (9, 39, 20)))

#
# p = (10, 41, 23)
# q = (21,36,23)
#
# # WE want difference between each of the couple of points
# print([x - y for x, y in zip(p,q)])
#
# # Get the squared differences
# print([(x - y) **2  for x, y in zip(p,q)])
#
# # Sum the differences up
# print(sum([(x - y) **2  for x, y in zip(p,q)]))
#
# # Then get square root of the sum of squared differences
# print(sqrt(sum([(x - y) **2  for x, y in zip(p,q)])))
#
