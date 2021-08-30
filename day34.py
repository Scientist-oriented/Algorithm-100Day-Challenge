import sys
sys.stdin=open("input.txt", "r")

'''
# 사용해야 하는 알고리즘 = bfs
    : 최단 거리로 가야하므로 bfs
    : 동서남북 탐색 대신 나이트의 이동 경로를 맞추어 탐색하면 됨.

# 문제 풀이 아이디어
    : 나이트는 한 위치에서 총 8가지로 움직일 수 있다.
    : 각각의 이동을 x, y +-로 짝지어 놓고 탐색하면 된다.

# 의사코드
    1. 입력을 받고 I**2의 인접 배열을 선언한다.
    2. 나이트의 이동 방법에 맞추어 x, y 좌표의 변경 쌍을 미리 선언해둔다.
    3. 시작 좌표를 queue에 넣고 bfs를 실시한다.
        3-1. 8방향 탐색 중에 0을 만나면 큐에 넣고 인접 배열에 이동할 때 걸린 횟수를 기록한다.
        3-2. pop한 결과가 도착 좌표와 동일하면 횟수를 출력한다.

'''
from collections import deque

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

T = int(input())

for _ in range(T):
    I = int(input())
    board = [[0 for _ in range(I)] for _ in range(I)]
    sx, sy = map(int, input().split())
    tx, ty = map(int, input().split())
    dq = deque()
    dq.append((sx, sy))
    board[sy][sx] = 1
    stop = False
    while not stop:
        x, y = dq.popleft()
        if x == tx and y == ty:
            print(board[y][x] - 1)
            stop = True
            break
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < I and 0 <= ny < I and board[ny][nx] == 0:
                dq.append((nx, ny))
                board[ny][nx] = board[y][x] + 1


'''
# 사용해야 하는 알고리즘 = bfs
    : 사실상 최단거리 문제와 동일한데
    : 출발점이 여러개고 목적지가 있는 것이 아니라
    : 모든 좌표에 도착할 때 끝난다.

# 문제 풀이 아이디어
    : 어차피 0 (안익은 토마토)가 있는지 board를 완전탐색해야 하므로
    : board에 각 위치의 토마토가 언제 익는지 표시하면서 bfs를 돌리면 된다.

# 의사 코드
    1. 입력을 받고 인접 배열을 완전 탐색하면서 익은 토마토의 좌표를 큐에 넣는다.
    2. 1의 큐를 가지고 bfs를 실시한다.
        2-1. 4방향 탐색을 하면서 안익은 토마토를 만나면
            2-1-1. 그 토마토에 현재 토마토 숫자에 + 1을 해서 board에 기록하고
            2-1-2. 큐에 추가한다.
        2-2. 큐가 빌 때까지 진행한다.
    3. board를 완전 탐색을 하면서
        3-1. board에 0이 있으면 바로 -1을 리턴하고
        3-2. board[y][x] > 0 이면 result에 계속 최댓값을 갱신한다.
    4. 0일차 익은 토마토가 1이므로 result - 1 리턴한다.
    5. 리턴 값을 출력한다.
'''
# from collections import deque
# M, N = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(N)]
# dq = deque()

# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]

# def isValid(x, y):
#     if x >= 0 and x < M and y >= 0 and y < N:
#         return True
#     else:
#         return False

# def bfs():
#     while dq:
#         x, y = dq.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if isValid(nx, ny) and board[ny][nx] == 0:
#                 board[ny][nx] = board[y][x] + 1
#                 dq.append((nx, ny))
#     result = 0
#     for i in range(M):
#         for j in range(N):
#             if board[j][i] == 0:
#                 return -1
#             elif board[j][i] > 0:
#                 result = max(board[j][i], result)
#     return result - 1

# for i in range(M):
#     for j in range(N):
#         if board[j][i] == 1:
#             dq.append((i, j))

# print(bfs())

'''
# 사용해야 하는 알고리즘 = bfs
    : 최단 경로 문제이므로 bfs

# 첫 풀이에 틀린 이유
    : 방문체크를 벽을 부순 경우와 부수지 않은 경우를
    : 별도로 해야 하는데 하나의 인접 배열에 처리했다.
    : 블로그를 찾아보니 방문 자체를 3차원 배열로 만들어서 처리했다.
        : x, y, z(벽뚫여부를 0, 1)를 저장해 놓고 visited[z][y][x] 이런 식으로 확인

# 문제 풀이 아이디어
    : bfs로 최단거리를 구하는데
    : queue에 좌표를 넣을 때 벽을 뚫었는지 여부를 기록한다.

# 의사코드
    1. 입력을 받는다. 방문 체크 인접 배열은 2개 선언한다.
    2. bfs를 실시한다.
        2-1. queue에 좌표를 넣을 때 벽을 뚫었는지 여부를 확인한다.
        2-2. pop한 좌표가 벽을 안뚫었다면
            2-2-1. 4 방향 탐색에서 벽을 만나면 뚫고 벽 뚫은 방문 체크를 한다.
            2-2-2. 길은 만나면 벽 안 뚫은 방문 체크를 한다.
        2-3. pop한 좌표가 벽을 뚫었다면
            2-3-1. 4방향 탐색에서 길을 만났을 때만 방문한다.
        2-4. 4방향 탐색 중에 최종 목적지를 만나면 리턴한다.
    3. 큐가 다 비었는데 목적지를 만나지 못하면 -1을 리턴한다.
'''
# from collections import deque
# N, M = map(int, input().split())
# board = [list(input()) for _ in range(N)]
# visited = [[False for _ in range(M)] for _ in range(N)]
# visitedWithB = [[False for _ in range(M)] for _ in range(N)]

# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]

# def isValid(x, y):
#     if x >= 0 and x < M and y >= 0 and y < N:
#         return True
#     else:
#         return False

# def bfs():
#     if N == 1 and M == 1:
#         return 1
#     dq = deque()
#     dq.append((0, 0, 1, False))
#     visited[0][0] = True
#     while dq:
#         x, y, t, b = dq.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx == M - 1 and ny == N - 1:
#                 return t + 1
#             if isValid(nx, ny):
#                 if not b and not visited[ny][nx]:
#                     if board[ny][nx] == "0":
#                         dq.append((nx, ny, t + 1, b))
#                         visited[ny][nx] = True
#                     else:
#                         dq.append((nx, ny, t + 1, True))
#                         visitedWithB[ny][nx] = True
#                 elif b and not visitedWithB[ny][nx]:
#                     if board[ny][nx] == "0":
#                         dq.append((nx, ny, t + 1, b))
#                         visitedWithB[ny][nx] = True
#     return -1

# print(bfs())

# bfs는 모든 경로가 동시에 출발하는 것과 같다.
    # queue에서 나중에 나오는 것이 더 빠를 확률은 0
# 벽 뚫은 방문 배열을 별도로 써야한다.
    # 벽을 뚫고 간 곳을 벽을 안 뚫고도 갈 수 있는 경우도 고려해야함!
    # bfs가 최단 시간을 보장하지만 벽을 안뚫고 갔다가
    # 나중에 뚫는 것이 더 유리할 수 있기 때문에!






'''
# 사용해야 하는 알고리즘 = bfs
    : 불 문제와 마찬가지고 2개의 큐를 가지고
    : bfs를 실시하면서 이동가능여부와 최단거리를 계산해야 한다.

# 문제 풀이 아이디어
    : 물 먼저 bfs하고
    : 고슴도치이 나중에 bfs하면 된다.
    : 단, 1초씩 번갈아 가면서 해야 한다! (큐 2개 사용)

# 의사코드
    1. 입력을 받고 visited를 표시할 인접배열을 선언한다.
    2. 큐를 2종류 선언한다. (고슴도치용, 물용)
    3. "S"의 좌표를 고슴도치 큐에 넣고 "*"의 좌표를 물 큐에 넣는다.
    4. 두 큐를 이용해서 번갈아서 bfs를 실시하는데 1초씩 번갈아서 해야하므로
        4-1. 큐에 추가할 때 바로 큐에 넣지 않고
        4-2. 임시로 빈 큐에 넣어두었다가 큐가 비면 bfs를 종료하고
        4-3. 임시 큐의 좌표를 큐에 옮기고 다른 bfs를 실시한다.
        4-4. 고슴도치 큐에 넣을 때는 시간도 함께 넣는다.
    5. bfs는 고슴도치 큐에 더 이상 추가될 좌표가 없을 때까지 실시한다.
        5-1. 고슴도치 큐에서 bfs를 하다가 "D"를 만나면
        5-2. pop된 시간에 +1 해서 리턴한다.
    6. 리턴된 결과를 출력한다.
    7. 고슴도치 큐가 빌 때까지 결과가 리턴 안되면 해당 문자열을 출력한다.

# 메모리 초과 계속 났던 이유
    : 메모리 초과는 보통 자료구조에서 데이터를 제대로 빼지 않거나
    : 중복된 데이터를 계속 넣고 있어서 그렇다.
    : and board[nr][nc] != "*"를 빼먹어서 그랬다.
'''
# from collections import deque
# R, C = map(int, input().split())
# board = [list(input()) for _ in range(R)]

# dr = [1, -1, 0, 0]
# dc = [0, 0, 1, -1]

# def isValid(r, c):
#     if r >= 0 and r < R and c >= 0 and c < C:
#         return True
#     else:
#         return False

# def bfs():
#     global dq, wdq
#     while dq:
#         temp = deque()
#         while wdq:
#             r, c = wdq.popleft()
#             for i in range(4):
#                 nr = r + dr[i]
#                 nc = c + dc[i]
#                 if isValid(nr, nc) and board[nr][nc] != "X" and board[nr][nc] != "D" and board[nr][nc] != "*":
#                     board[nr][nc] = "*"
#                     temp.append((nr, nc))
#         wdq = temp
#         temp = deque()
#         while dq:
#             r, c, t = dq.popleft()
#             for i in range(4):
#                 nr = r + dr[i]
#                 nc = c + dc[i]
#                 if isValid(nr, nc) and not visited[nr][nc] and board[nr][nc] != "*" and board[nr][nc] != "X":
#                     if board[nr][nc] == "D":
#                         return t + 1
#                     else:
#                         visited[nr][nc] = True
#                         temp.append((nr, nc, t + 1))
#         dq = temp
#     return False

# dq = deque()
# wdq = deque()
# visited = [[False for _ in range(C)] for _ in range(R)]
# for i in range(R):
#     for j in range(C):
#         if board[i][j] == "S":
#             dq.append((i, j, 0))
#         elif board[i][j] == "*":
#             wdq.append((i, j))

# result = bfs()

# print(result if result else "KAKTUS")



'''
# 사용해야 하는 알고리즘 = bfs
    : 건물을 탈출하는 최단 시간을 구하려면
    : bfs로 최단거리를 구하는 방식을 동일하게 사용하면 된다.

# 첫 풀이에 실패한 이유
    : 처음에 사람이 가는 것만 bfs로 하고
    : 불이 번지는 것은 매번 모든 불에 대해서 동서남북 탐색을 했다.
    : 그래서 계속 메모리 초과가 난 것 같다.
    : 결국 블로그 찾아봄.

# 문제 풀이 아이디어
    : 불 먼저 (앞으로 번질 지역은 못가므로) bfs하고
    : 사람이 나중에 bfs하면 된다.
    : 단, 1초씩 번갈아 가면서 해야 한다!

# 의사코드
    1. 입력을 받고 visited를 표시할 인접배열을 선언한다.
    2. 큐를 2종류 선언한다. (사람용, 불용)
    3. "@"의 좌표를 사람 큐에 넣고 "*"의 좌표를 불 큐에 넣는다.
    4. 두 큐를 이용해서 번갈아서 bfs를 실시하는데 1초씩 번갈아서 해야하므로
        4-1. 큐에 추가할 때 바로 큐에 넣지 않고
        4-2. 임시로 빈 큐에 넣어두었다가 큐가 비면 bfs를 종료하고
        4-3. 임시 큐의 좌표를 큐에 옮기고 다른 bfs를 실시한다.
        4-4. 사람 큐에 넣을 때는 시간도 함께 넣는다.
    5. bfs는 사람 큐에 더 이상 추가될 좌표가 없을 때까지 실시한다.
        5-1. 중간에 인접배열의 가장자리 좌표에 도착하면 (= 건물 최외곽)
        5-2. pop된 시간에 +1 해서 리턴한다.
    6. 리턴된 결과를 출력한다.
    7. 테스트 케이스만큼 돌면서 1 ~ 6를 반복한다.
'''

# from collections import deque

# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]

# T = int(input())

# def isValid(x, y):
#     if x >= 0 and x < w and y >= 0 and y < h:
#         return True
#     else:
#         return False

# def isEscaped(x, y):
#     if x == 0 or y == 0 or x == w - 1 or y == h - 1:
#         return True
#     else:
#         return False

# def bfs():
#     global dq, fdq
#     while dq:
#         temp = deque()
#         while fdq:
#             x, y = fdq.popleft()
#             for i in range(4):
#                 nx = x + dx[i]
#                 ny = y + dy[i]
#                 if isValid(nx, ny) and board[ny][nx] != "#" and board[ny][nx] != "*":
#                     temp.append((nx, ny))
#                     board[ny][nx] = "*"
#         fdq = temp
#         temp = deque()
#         while dq:
#             x, y, t = dq.popleft()
#             if isEscaped(x, y): return t + 1
#             for i in range(4):
#                 nx = x + dx[i]
#                 ny = y + dy[i]
#                 if isValid(nx, ny) and not visited[ny][nx] and board[ny][nx] == ".":
#                     temp.append((nx, ny, t + 1))
#                     visited[ny][nx] = True
#         dq = temp
#     return None
    


# for _ in range(T):
#     w, h = map(int, input().split())
#     board = [list(input()) for _ in range(h)]
#     visited = [[False for _ in range(w)] for _ in range(h)]
#     dq = deque()
#     fdq = deque()
#     for i in range(w):
#         for j in range(h):
#             if board[j][i] == "@":
#                 dq.append((i, j, 0))
#                 visited[j][i] = True
#             elif board[j][i] == "*":
#                 fdq.append((i, j))
#     result = bfs()
#     print(result if result != None else "IMPOSSIBLE")


