'Making a message publisher/subscriber service'

from typing import List, Tuple, DefaultDict, Set, Optional, NamedTuple, Deque, Dict
from collections import deque, defaultdict
import hashlib
import random
import secrets
from itertools import islice
from time import time, sleep
from heapq import merge
from bisect import bisect
from sys import intern
import pickle
import re

User = str
Timestamp = str
Post = NamedTuple('Post', [('timestamp', str), ('user', str), ('text', str)])

posts = deque()  # type: deque
user_posts = defaultdict(deque)  # type: DefaultDict[User, deque]
following = defaultdict(set)
followers = defaultdict(set)


def post_message(user, text, timestamp) -> None:
    user = intern(user) # make sure it gets used only one time
    timestamp = timestamp or time.time()
    post = Post(timestamp, user, text)
    posts.append(post)
    user_posts[user].append(post)


def follow(user, followed_user) -> None:
    user, followed_user = intern(user), intern(followed_user)
    following[user].add(followed_user)
    followers[followed_user].add(user)


def posts_by_users(user: User, limit: Optional[int] = None):
    return list(islice(user_posts[user], limit))


def post_for_user(user: User, limit: Optional[int] = None) -> List[Post]:
    relevant = merge(*[user_posts[followed_user]
                       for followed_user in following[user]], reverse = True)
    return list(islice(relevant, limit))


def search(phrase: str, limit: Optional[int] = None) -> List[Post]:
    # TODO : add pre-indexing to speed up searches
    # TODO: Add time sensitive caching of search queries
    return list(islice((post for post in posts if phrase in post.text), limit))
