from itertools import combinations

arr = ["a", "a", "z", "z"]

for word in combinations(arr,4):
    print(word)

