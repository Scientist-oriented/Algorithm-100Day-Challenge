from itertools import groupby

a = ['A', 'A', 'B', 'B', 'B', 'C', 'D', 'A']

maxCandy = 0
for val, group in groupby(a):
    print(val, list(group))