
from __future__ import  annotations
import sys
from collections import Counter, defaultdict


from typing import cast

from typing_extensions import reveal_type

Vector = list[float]
txt = "This is a vast world you can't traverse world in a day"
def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]


new_vector = scale(2.0, [1.0, -4.2,5.4])
print(new_vector)

v = list[float]
v = [5,3,4]
print(v)
t = tuple()
t = (3,2)
print(t)
s = set()
s = {1,5,3,3}
print(s)

c = [sys.executable]
print(c[0])

counts = Counter(txt.split())
print(counts)
print(counts.most_common(2))

def greeting(name: str) -> str:
    return 'Hello' + name

lists = [[]] * 3
lists[0].append(3)
print(lists)

rd = defaultdict(list)
for name, num in [('ichi',1),('one',1),('two',1),('tree',1),('four',1),('five',1)]:
    rd[num].append(name)
print(rd)
rd[2].append('two')
print(rd)
l= [ 1,4,5,6,7,8,9 ]
print(min(l))
print(max(l))

x = 1
reveal_type(x)
y = cast(str,x)
reveal_type(y)
y.upper()