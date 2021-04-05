import sys
sys.stdin=open("input.txt", "r")


'''

# 점화식 = 특정 함수를 더 작은 변수에 대한 함수의 관계로 표현한 것!

# 이취코 p.142 DFS 구현

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

dfs(graph, 1, visited)


# 이취코 p.118 복습

n, m = map(int, input().split())
mapArray = list()

a, b, d = map(int, input().split())

for _ in range(n):
    row = list(map(int, input().split()))
    mapArray.append(row)

da = [-1, 0, 1, 0]
db = [0, 1, 0, -1]

def turn_left():
    global d
    d -= 1
    if d < 0:
        d = 3

mapArray[a][b] = 2

turn_times = 0
count = 1

while True:
    turn_left()
    turn_times += 1
    na = a + da[d]
    nb = b +db[d]
    if mapArray[na][nb] == 0:
        a = na
        b = nb
        count += 1
    else:
        if turn_times < 4:
            continue
        else:
            na = a - da[d]
            nb = b - db[d]
            if mapArray[na][nb] == 1:
                break
            else:
                a = na
                b = nb
                turn_times = 0

print(count)
'''