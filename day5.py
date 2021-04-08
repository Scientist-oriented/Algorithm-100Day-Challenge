import sys
sys.stdin=open("input.txt", "r")
# 백준 18352
    # 내일 다시!
from collections import deque

n, m, k, x = map(int, input().split())

graph = [[]] * (n + 1)
visited = [False] * (n + 1)

for _ in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)

def bfs(start):
    queue = deque()
    queue.append(start)
    count = 0

    while queue:
        city = queue.popleft()
        print(city, count, "POP")
        visited[city] = count
        count += 1

        for next_city in graph[city]:
            if visited[next_city] <= count:
                queue.append(next_city)

bfs(1)
print(visited)


'''
# 이취코 p.152 미로탈출
from collections import deque
n, m = map(int, input().split())

graph = list()
for _ in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    # 따로 visited를 쓸 필요가 없는 것이 그냥 지도에 바로 표시하면 된다.
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n - 1][m - 1]

print(bfs(0, 0))
'''


