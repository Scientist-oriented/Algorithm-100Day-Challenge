import sys
sys.stdin=open("input.txt", "r")

'''
# 사용해야 하는 알고리즘 = dfs 혹은 bfs (완전탐색)
    : 다른 이어지는 영역구하는 문제와 마찬가지로
    : 완전 탐색이 필요하다.

# 문제 풀이 아이디어
    : 그림을 인접 행렬로 입력을 받은 다음에
    : 방문 표시를 하면서 dfs를 돌면 된다.
    : 단! 적록색약 / 비적록색약 2개의 dfs를 돌아서 비교해야 한다!

# 의사코드
    1. 입력을 받는다 인접 행렬을 2가지 준비한다. (deepcopy)
    2. 하나의 인접 행렬은 그대로 사용하고
        2-1. 다른 하나의 인접행렬은 반복문을 돌아 G를 R로 바꾼다.
    3. 두 인접행렬을 dfs를 돌면서 영역의 갯수를 저장한다.
        3-1. dfs를 돌 때 현재 color 값도 같이 넘겨서 같은 색만 dfs를 돌면서 방문체크하도록 한다.
    4. 결과를 출력한다.

# 시간 복잡도
    : 모든 정점을 방문하고 각 정점마다 동서남북 4번의 반복문 실행
    : 최대 O(4n**n) = O(n**2)
    : 추가로 이중 반복문 O(n**2)이 두 개 있는데 n이 최대 100이므로 안전!

# 구글링 내용
    : board를 입력 받아서 deepcopy해서 2개로 만들어서 했는데
        : board에 직접 방문체크를 해가면서 했기 때문에
    : 코드가 너무 길어져서 (dfs 함수를 두번 정의 해야했음...) 이건 아니다 싶어 구글링
    : 찾아본 결과 방문 체크용 행렬을 별도로 만들면 코드를 줄일 수 있었음.
'''
import copy

n = int(input())
board1 = []
for _ in range(n):
    board1.append(list(input()))

board2 = copy.deepcopy(board1)
for i in range(n):
    for j in range(n):
        if board2[j][i] == "G":
            board2[j][i] = "R"

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def isValid(x, y):
    if x >= 0 and x < n and y >= 0 and y < n:
        return True
    else:
        return False

def dfs1(x, y, color):
    global board1
    board1[y][x] = 0
    stack = []
    stack.append((x, y))
    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if isValid(nx, ny) and board1[ny][nx] == color:
                board1[ny][nx] = 0
                stack.append((nx, ny))

def dfs2(x, y, color):
    global board2
    board2[y][x] = 0
    stack = []
    stack.append((x, y))
    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if isValid(nx, ny) and board2[ny][nx] == color:
                board2[ny][nx] = 0
                stack.append((nx, ny))

result1 = 0
result2 = 0
for i in range(n):
    for j in range(n):
        if board1[j][i] != 0:
            dfs1(i, j, board1[j][i])
            result1 += 1

for i in range(n):
    for j in range(n):
        if board2[j][i] != 0:
            dfs2(i, j, board2[j][i])
            result2 += 1

print(result1, result2)
'''
# 사용해야 하는 알고리즘 = dfs 혹은 bfs (완전탐색)
    : 1, 2번과 마찬가지로 직사각형이 차지하지 않는 영역의 갯수와 크기를 구하려면
    : 완전 탐색을 통해서 연결된 빈칸을 찾아야 한다.

# 문제 풀이 아이디어
    : 인접행렬로 모눈종이의 한칸한칸을 표현하고
    : 직사각형이 들어간 모든 곳에 표시를 한다.
    : 그 후 표시안된 모눈이 나올 때 완전탐색을 한다.

# 의사코드
    1. 입력을 받는다.
    2. n * m의 인접행렬을 만든다.
    3. 직사각형의 좌표를 받아서 인접행렬에 표시한다.
        3-1. x1 이상 x2미만이고
        3-2. y1 이상 y2미만인 모눈에 모두 표시한다.
    4. 인접행렬의 [0][0]부터 돌면서 dfs를 실시한다.
        4-1. dfs를 돌면서 빈칸의 갯수를 세고
        4-2. 끝나면 빈칸의 갯수를 리턴해서 빈배열에 저장한다.
    5. 배열에 있는 영역의 갯수와 배열을 오름차순으로 정렬한 것을 출력한다.

# 시간 복잡도
    : 모든 정점을 방문하고 각 정점마다 동서남북 4번의 반복문 실행
    : 최대 O(4 n**m) = O(n**2)
    : 추가로 이중 반복문 O(n ** m)이 있는데 n, m이 최대 100이기 때문에 안전! 
'''
# m, n, k = map(int, input().split())
# board = [[0 for _ in range(n)] for _ in range(m)]
# for _ in range(k):
#     x1, y1, x2, y2 = map(int, input().split())
#     for i in range(x1, x2):
#         for j in range(y1, y2):
#             board[j][i] = 1

# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]

# def isValid(x, y):
#     if x >= 0 and x < n and y >= 0 and y < m:
#         return True
#     else:
#         return False

# def dfs(x, y):
#     global board
#     stack= []
#     board[y][x] = 1
#     stack.append((x, y))
#     cnt = 1
#     while stack:
#         x, y = stack.pop()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if isValid(nx, ny) and board[ny][nx] == 0:
#                 board[ny][nx] = 1
#                 stack.append((nx, ny))
#                 cnt += 1
#     return cnt
# results = []
# for i in range(n):
#     for j in range(m):
#         if board[j][i] == 0:
#             result = dfs(i, j)
#             results.append(result)

# print(len(results))
# for result in sorted(results):
#     print(result, end=" ")



'''
# 사용해야 하는 알고리즘 = dfs 혹은 bfs (완전탐색)
    : 음식 문제와 마찬가지로 연결된 집을 찾으려면
    : 완전 탐색을 통해서 연결된 모든 집을 찾아야 한다.

# 문제 풀이 아이디어
    : 지도를 행렬로 저장하고
    : 집이 나오면 동서남북 완전탐색하고 (방문체크)
    : 단지 수를 센다.

# 의사코드
    1. 지도 입력을 받는다.
    2. 지도의 모든 좌표를 이중반복문으로 돌면서
        2-1. 집을 만나면 dfs를 실시한다.
            2-1-1. dfs를 실시하면서 연결된 집의 갯수를 세고
            2-1-2. 방문 표시를 한다.
        2-2. dfs에서 반환된 집의 갯수를 빈 배열에 저장한다.
    3. 결과물 배열을 오름 차순으로 정렬하고 출력한다.

# 시간 복잡도
    : 모든 정점을 방문하고 각 정점마다 동서남북 4번의 반복문 실행
    : 최대 O(4 n**n) = O(n**2)
    : 추가로 이중 반복문 O(n ** n)이 있는데 n이 최대 25이기 때문에 안전! 
'''
# import sys
# input = sys.stdin.readline

# dr = [1, -1, 0, 0]
# dc = [0 , 0 , 1, -1]

# def isValid(r, c):
#     if r >= 0 and r < n and c >= 0 and c < n:
#         return True
#     else:
#         return False

# n = int(input())
# board = [list(input()) for _ in range(n)]

# def dfs(r, c):
#     stack = []
#     stack.append((r, c))
#     board[r][c] = 0
#     size = 1
#     while stack:
#         r, c = stack.pop()
#         for i in range(4):
#             nr = r + dr[i]
#             nc = c + dc[i]
#             if isValid(nr, nc) and board[nr][nc] == "1":
#                 stack.append((nr, nc))
#                 board[nr][nc] = 0
#                 size += 1
#     return size

# result = []

# for i in range(0, n):
#     for j in range(0, n):
#         if board[i][j] == "1":
#             currentSize = dfs(i, j)
#             result.append(currentSize)

# print(len(result))
# for num in sorted(result):
#     print(num)


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

# 시간복잡도
    : 모든 정점을 방문하고 각 정점마다 동서남북 4번의 반복문 실행
    : 즉 O(4k) = O(k)
    : 이중 반복문 O(n * m)이 있는데 이것은 최대 O(100000)이기 때문에 안전!
'''
# import sys
# input = sys.stdin.readline

# dr = [1, -1, 0, 0]
# dc = [0 , 0 , 1, -1]

# def isValid(r, c):
#     if r >= 0 and r < n + 1 and c >= 0 and c < m + 1:
#         return True
#     else:
#         return False

# n, m, k = map(int, input().split())
# board = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
# for _ in range(k):
#     r, c = map(int, input().split())
#     board[r][c] = 1

# def dfs(r, c):
#     stack = []
#     stack.append((r, c))
#     board[r][c] = 0
#     size = 1
#     while stack:
#         r, c = stack.pop()
#         for i in range(4):
#             nr = r + dr[i]
#             nc = c + dc[i]
#             if isValid(nr, nc) and board[nr][nc] == 1:
#                 stack.append((nr, nc))
#                 board[nr][nc] = 0
#                 size += 1
#     return size

# result = 0

# for i in range(1, n + 1):
#     for j in range(1, m + 1):
#         if board[i][j] == 1:
#             currentSize = dfs(i, j)
#             result = max(result, currentSize)

# print(result)