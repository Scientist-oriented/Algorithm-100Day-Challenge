import sys
sys.stdin=open("input.txt", "r")

'''
# 사용해야 하는 알고리즘 = dfs 혹은 bfs (완전탐색)
    : 연결된 음식 1개를 찾기 위해서는 완전 탐색을 통해서
    : 한 음식으로 부터 연결된 모든 음식을 찾아야 한다.

# 문제 풀이 아이디어
    : n * m 짜리 행렬을 만들고 좌표를 표시해서
    : 음식이 나오면 완전탐색하고
    : 탐색하는 동안 연결된 음식 갯수를 센다.

# 의사코드
    1. n * m 행렬을 선언한다.
    2. 음식물 쓰레기 좌표를 받아서 행렬에 표시한다.
    3. 표시한 행렬을 이중 반복문으로 모든 좌표를 돌면서
        3-1. 음식을 만나면 dfs를 실시한다.
            3-1-1. dfs를 실시하면서는 연결된 음식 갯수를 세고
            3-1-2. 연결된 음식은 방문 표시를 한다.
        3-2. dfs에서 반환된 음식의 갯수를 현재 최댓값과 비교해서 갱신한다.
    4. 최댓값을 출력한다.
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

dr = [1, -1, 0, 0]
dc = [0 , 0 , 1, -1]

def isValid(r, c):
    if r >= 0 and r < n + 1 and c >= 0 and c < m + 1:
        return True
    else:
        return False

n, m, k = map(int, input().split())
board = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
for _ in range(k):
    r, c = map(int, input().split())
    board[r][c] = 1

def dfs(r, c, size):
    board[r][c] = 0
    size += 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if isValid(nr, nc) and board[nr][nc] == 1:
            dfs(nr, nc, size)
    return size

result = 0

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if board[i][j] == 1:
            currentSize = dfs(i, j, 0)
            result = max(result, currentSize)

print(result)

'''
bfs에서 queue에 넣을 때 distance를 같이 queue에 넣어서 기록한다.
'''

# from collections import deque
# dx = [1, -1, 0, 0]
# dy = [0 , 0 , 1, -1]

# n, m = map(int, input().split())
# board = [list(input()) for _ in range(n)]
# visited = [[False for _ in range(m)] for _ in range(n)]

# def isValid(x, y):
#     if x >= 0 and x < m and y >= 0 and y < n and board[y][x] == "1":
#         return True
#     else:
#         return False

# def bfs(x, y, d):
#     global visited
#     dq = deque()
#     dq.append((x, y, d))
#     visited[y][x] = True
#     while dq:
#         x, y, d = dq.popleft()
#         if x == m - 1 and y == n - 1:
#             print(d)
#             return
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if isValid(nx, ny) and not visited[ny][nx]:
#                 dq.append((nx, ny, d + 1))
#                 visited[ny][nx] = True

# bfs(0, 0, 1)
'''
1. 방문체크 하면서 완전탐색
2. 완전 탐색 할 때마다 cnt += 1
'''
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10000)

# def dfs(node):
#     global checks
#     checks[node] = True
#     for i in range(1, n + 1):
#         if vertices[node][i] == 1 and not checks[i]:
#             dfs(i)

# n, m = map(int, input().split())
# checks = [False] * (n + 1)
# vertices = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

# for _ in range(m):
#     s, e = map(int, input().split())
#     vertices[s][e] = 1
#     vertices[e][s] = 1

# cnt = 0

# for i in range(1, n + 1):
#     if not checks[i]:
#         cnt += 1
#         dfs(i)

# print(cnt)


