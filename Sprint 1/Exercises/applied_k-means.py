import glob
import os
from kmeans import k_means, assign_data
import csv
from collections import namedtuple, defaultdict, Counter
from pprint import pprint
import glob
from typing import *


NUM_SENATORS = 100

folder_path = '/congress_data'

# create a class for isntances of a senator
Senator = namedtuple('Senator', ['name','party','state'])

#convert strings to numerics
vote_values = {'Yea': 1, 'Nay': -1, 'Not Voting': 0}

# accumulate with defaultdict
accumulated_record = defaultdict(list)

# use glob to get all files within the folder

#load votes which were accumulated by senator
for filename in glob.glob(f'{folder_path}/congress_votes*.csv'):
    with open(filename, encoding= 'utf-8') as f:
        reader = csv.reader(f)

        #use next to get directly to the data
        vote_topic = next(reader)
        headers = next(reader)

        # unpacking all rows
        for person,state, district, vote, name, party in reader:
            senator = Senator(name, party, state)
            accumulated_record[senator].append(vote_values[vote])

# pprint(accumulated_record, width = 400)

# the yea and not voting etc need to be numeric values
# transform the record into a plain dict that maps to tuple of votes
record = {senator: tuple(votes) for senator, votes in accumulated_record.items()}   #type: Dict[Senator, VoteHistory]

# use k-means to locate the cluster centroid from pattern of votes, assign each senator to the nearest centroid
centroids = k_means(record.values(), k = 3)
clustered_votes = assign_data(centroids, record.values())

# for centroid in centroids:
#     for x in centroid:
#         print(f'{x:.2f}', end = ' ')
#     print()

#build a reverse mapping from a vote history to a list of senators who voted that way
votes_to_senators = defaultdict(list)       #type: DefaultDict[VoteHistory, List[Senator]]

for senator, vote_hist in record.items():
    votes_to_senators[vote_hist].append(senator)

assert sum([len(cluster) for cluster in votes_to_senators.values()]) == NUM_SENATORS

# Display all the clusters and the members (senators) of each of the clusters

for i, votes_in_cluster in enumerate(clustered_votes.values(), start = 1):
    print(f'======================== Voting Cluster #{i} =================')
    print()
    party_totals = Counter()
    for votes in set(votes_in_cluster):
        # take a senators voting history and take it back to the list of senators
        for senator in votes_to_senators[votes]:
            party_totals[senator.party] += 1
            print(senator)
    print(party_totals)

#k-means we need to ask if we are clustering votes of equal importance or different, we could change the votes weight
# also what would we have to do in not voting, can they maybe be different values? based on nature of voting
# using only passed bills might bias the results
# method we use assumes patterns in affiliations, but these do not change over time
# random starts to the use give different results
# binary vectors may give more sense, include more years and get better differentiations