import sys
sys.stdin=open("input.txt", "r")

# 이취코 p.335 외벽점검 내코드

'''
# 이취코 p.332 치킨 배달 답코드
from itertools import combinations

n, m = map(int, input().split())

vil = []
for _ in range(n):
    row = list(map(int, input().split()))
    vil.append(row)

houses = []
stores = []
for r in range(len(vil)):
    for c in range(len(vil[0])):
        if vil[r][c] == 1:
            houses.append((r + 1, c + 1))
        elif vil[r][c] == 2:
            stores.append((r + 1, c + 1))

candidates = list(combinations(stores, m))

def chickenDistance(candidate):
    result = 0
    for house in houses:
        hx, hy = house
        temp = int(1e9)
        for store in candidate:
            sx, sy = store
            currentDistance = abs(hx - sx) + abs(hy - sy)
            temp = min(temp, currentDistance)
        result += temp
    return result

answer = int(1e9)
for candidate in candidates:
    answer = min(answer, chickenDistance(candidate))

print(answer)

# 이취코 p.332 치킨 배달 내코드 -> 풀이 실패
import heapq

n, m = map(int, input().split())


vil = []
for _ in range(n):
    row = list(map(int, input().split()))
    vil.append(row)

houses = []
stores = []
for r in range(len(vil)):
    for c in range(len(vil[0])):
        if vil[r][c] == 1:
            houses.append((r + 1, c + 1))
        elif vil[r][c] == 2:
            stores.append([0, r + 1, c + 1])

storeDistance = []

for store in stores:
    totalDistance = 0
    for house in houses:
        totalDistance += abs(store[0] - house[0]) + abs(store[1] - house[1])
    totalDistance = -totalDistance
    heapq.heappush(storeDistance, (totalDistance, store[0], store[1]))

print(storeDistance)

while len(stores) > m:
    closedstore = heapq.heappop(storeDistance)
    stores.remove((closedstore[1], closedstore[2]))

print(stores)

result = 0

for house in houses:
    chickenDistance = int(1e9)
    for store in stores:
        currentDistance  = abs(store[0] - house[0]) + abs(store[1] - house[1])
        chickenDistance = min(currentDistance, chickenDistance)
    result += chickenDistance

print(result)
'''