import sys
sys.stdin=open("input.txt", "r")

# 다익스트라 알고리즘: 간단한 버전
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n + 1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i 
    return index

'''

# 이취코 p.226 효율적인 화폐 구성 - 답
n, m = map(int, input().split())

array = []
for i in range(n):
    array.append(int(input()))

d = [10001] * (m + 1)

d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        if d[j - array[i]] != 10001:
            d[j] = min(d[j], d[j - array[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])


# 이취코 p.226 효율적인 화폐 구성 - 내 풀이
n, m = map(int, input().split())
coins = list()

for _ in range(n):
    coin = int(input())
    coins.append(coin)

d = [10001] * (m + 1)

for coin in coins:
    d[coin] = 1

for i in range(0, m + 1): # 가장 작은 코인부터 해야한다.
    for coin in coins:
        if d[i - coin] < 10001:
            d[i] = min(d[i], d[i - coin] + 1)

if d[m] < 10001:
    print(d[m])
else:
    print(-1)

# 이취코 p.223 바닥 공사 - 답
n = int(input())
d = [0] * 1001

d[1] = 1
d[2] = 3

for i in range(3, n + 1):
    d[i] = (d[i - 1] + d[i - 2] * 2) % 796796

print(d[n])


# 이취코 p.220 개미 전사 - 답
n = int(input())
array = list(map(int, input().split()))
d = [0] * 100
d[0] = array[0]
d[1] = max(array[0], array[1])

for i in range(3, n):
    d[i] = max(d[i - 1], d[i - 2] + array[i])

print(d[n - 1])


# 이취코 p.217 1로 만들기 - 답

x = int(input())

d = [0] * 30001

for i in range(2, x + 1):
    d[i] = d[i - 1] + 1

    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)

    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)

print(d[x])
'''