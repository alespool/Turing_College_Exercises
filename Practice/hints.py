from typing import *
from collections import OrderedDict, deque
import secrets

x = 10              # type: int


def f(x: int, y: Optional[int] = None) -> int:
    if y is None:
        y = 20
    return x + y


y = OrderedDict()   # type: OrderedDict


def g(x: List[int]) -> None:
    print(len(x))
    print(x[2])
    for i in x:
        print(i)
    print()


g([10, 20, 30, 50])


hts = [97.1, 102.5, 97.5]
person = ('Raymond', 5 * 12 + 11)
info = ('Pearson', 'Course', 'Python', 'Raymond')
fifo = deque()

Point = NamedTuple('Point', [('x', int) , ('y', int)])
print(Point)
