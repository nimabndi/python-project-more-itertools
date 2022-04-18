from itertools import count, repeat, chain, islice, tee, accumulate
from more import always_reversible
from operator import sub
from sys import version_info


l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
s = [0, 1, 3, 6, 7, 10]
#
# m = repeat(2)
# for i in m:
#     print(i)
# for i in range(-len(l), len(l)):
#     print(l[i])
m = l
l.pop()
print(m)

