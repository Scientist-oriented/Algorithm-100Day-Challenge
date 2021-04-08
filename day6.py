import sys
sys.stdin=open("input.txt", "r")

# 이취코 p.152 미로탈출
from collections import deque

n, m = map(int, input().split())

graph = []
for _ in range(n):
    row = list(map(int, input()))
    graph.append(row)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0  or ny >= m:
                continue
            
            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    
    return graph[n - 1][m - 1]

result = bfs(0, 0)
print(result)
