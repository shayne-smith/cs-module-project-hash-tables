import itertools
"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

# q = set(range(1, 10))
q = set(range(1, 200))
# q = (1, 3, 4, 7, 12)
lst = list(q)

cache = {}

def f(x):
    return x * 4 + 6


# def permutations(lst):

#     if len(lst) == 0:
#         return []

#     if len(lst) == 1:
#         return [lst]

#     l = []

#     for i in range(len(lst)):
#         m = lst[i]

#         remLst = lst[:i] + lst[i+1:]

#         for p in permutations(remLst):
#             l.append([m] + p)
#     return l

# def combinations(lst):
#     j = 0
#     count = 0

#     for i in range(len(lst)):
#         temp = lst[:j] + lst[j+1:]
#         for p in permutations(temp):
#             count += 1
#             print(p)
#             if p[0] + p[1] == p[2] - p[3]:
#                 cache[(p[0], p[1], p[2], p[3])] = (p[0], p[1], p[2], p[3])
#         j += 1
#     print(count)

# build cache with correct tuples
for p in itertools.product(lst, repeat=4):
    if f(p[0]) + f(p[1]) == f(p[2]) - f(p[3]):
        cache[(p[0], p[1], p[2], p[3])] = (f(p[0]), f(p[1]), f(p[2]), f(p[3]))

# print tuples that satisfy function
for k, v in cache.items():
    print(f"f({k[0]}) + f({k[1]}) = f({k[2]}) - f({k[3]})    {v[0]} + {v[1]} = {v[2]} - {v[3]}")
    




