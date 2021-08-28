import sys
sys.stdin=open("input.txt", "r")

'''
# 사용해야 하는 알고리즘 = bfs (최단 거리)
    : 어느 지점에서 목표 지점으로 가는 최단 거리는 bfs로 구한다.

# 문제 풀이 아이디어
    : 현재 위치에서 bfs를 한다.
    : 단, bfs를 하기 전에 불이 번진 것을 먼저 표시한다.
    : 출구가 몇개인지 어디 있는지 알 수 없으므로 
        : x 혹은 y 좌표가 가장자리에 위치하면 탈출한 것으로 간주한다.

# 중간 개선 사항
    1. 시간초과 : fire를 원래 이중 반복문으로 체크하면서 늘렸는데 좌표 압축으로
    2. 메모리 초과 : visited 따로 없이 
'''


from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

T = int(input())

def isValid(x, y):
    if x >= 0 and x < w and y >= 0 and y < h:
        return True
    else:
        return False

def isEscaped(x, y):
    if x == 0 or y == 0 or x == w - 1 or y == h - 1:
        return True
    else:
        return False

# def moreFire():
#     check = [[False for _ in range(w)] for _ in range(h)]
#     for fx in range(w):
#         for fy in range(h):
#             if board[fy][fx] == "*" and not check[fy][fx]:
#                 check[fy][fx] = True
#                 for i in range(4):
#                     nfx = fx + dx[i]
#                     nfy = fy + dy[i]
#                     if isValid(nfx, nfy) and board[nfy][nfx] != "#" and not check[nfy][nfx]:
#                         board[nfy][nfx] = "*"
#                         check[nfy][nfx] = True

def morefire(fires):
    newFires = []
    for fire in fires:
        x, y = fire
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if isValid(nx, ny) and board[ny][nx] != "#":
                newFires.append((nx, ny))
    return fires + newFires

def bfs(x, y, fires):
    dq = deque()
    dq.append((x, y, 0))
    board[y][x] = 1
    currentTime = 0
    fires = morefire(fires)
    while dq:
        x, y, t = dq.popleft()
        if t > currentTime:
            fires = morefire(fires)
            currentTime = t
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            nextPosition = (nx, ny)
            if isValid(nx, ny) and nextPosition not in fires and board[ny][nx] == ".":
                if isEscaped(nx, ny):
                    print(t + 2)
                    return
                else:
                    dq.append((nx, ny, t + 1))
                    board[ny][nx] = 1
    print("IMPOSSIBLE")
    return
    
for _ in range(T):
    w, h = map(int, input().split())
    board = [list(input()) for _ in range(h)]
    fires = []

    for i in range(w):
        for j in range(h):
            if board[j][i] == "*":
                fires.append((i, j))
    for i in range(w):
        for j in range(h):
            if board[j][i] == "@":
                bfs(i, j, fires)



'''
# 사용해야 하는 알고리즘 = bfs (최단 거리)
    : 어느 지점에서 목표 지점으로 가는 최단 거리는 bfs로 구한다.

# 문제 풀이 아이디어
    : 맨 S에서 출발해서 bfs로 최단거리를 기록하면서 간다.
    : 매번 bfs를 할 때 마다 상하동서남북 6방향을 확인한다.
    : E에 도달하면 도달한 시간을 출력하고
    : 완전탐색 이후에도 E에 도달하지 못하면 Trapped를 출력한다.

# 의사코드
    1. 입력을 받고 배열에 각 층별로 저장한다.
        1-1. 배열 = 인접행렬 * (층수)
    2. 맨 위층부터 bfs를 돌면서 최단 경로를 찾는다.
        2-1. queue에 저장할 때 걸린 시간을 같이 저장하고
        2-2. 매번 6방향 탐색을 할 때 마다 "E"에 도달했는지 확인한다.
    3. E를 만나면 시간을 출력하고 완전탐색 이후에도 E를 만나지 못하면 Trapped를 출력한다.

# 직접 코드 짜본 후 소감
    : 무조건 내려가는 방향으로 가는 것이 좋다고 생각했는데
    : 아닌 반례도 충분히 있으니 (윗층, 아래층에 벽이 있어서 내려갔다, 올라갔다, 다시 내려가야하는 경우)
    : 6방향 탐색을 해야함!

    : bfs 내부의 queue는 무조건 비용 오름 차순으로 정렬 되어있다. (시간이 적게 걸리는 것이 앞으로 오도록)
    : 즉 "E"를 만나면 더 이상 queue에 있는 것을 추가적으로 살펴보지 않아도 됨.
    
    : 중간에 메모리 초과 났는데 코드 고치다 보니되었음 ㅡㅡ;;;
'''
# from collections import deque

# dr = [1, -1, 0, 0, 0, 0]
# dc = [0, 0, 1, -1, 0, 0]
# dl = [0, 0, 0, 0, 1, -1]
#     # 🚫 이딴데서 오타나서 틀림!!!

# while True:
#     L, R, C = map(int, input().split())
#     if L == R == C == 0:
#         break

#     def isValid(l, r, c):
#         if l >= 0 and l < L and r >= 0 and r < R and c >= 0  and c < C:
#             return True
#         else:
#             return False

#     building = []
#     for _ in range(L):
#         floor = [list(input()) for _ in range(R)]
#         building.append(floor)
#         input() 
#         # 💡 빈 줄 하나 띄고 입력 받기

#     for i in range(L):
#         for j in range(R):
#             for k in range(C):
#                 if building[i][j][k] == "S":
#                     start = (i, j, k, 0)
#                     break
    
#     dq = deque()

#     dq.append(start)
#     l, r, c, t = start
#     building[l][r][c] = "#"

#     escaped = False
#     # 💡 이중반복문을 빠져나오기 위한 수단
#     while dq and not escaped:
#         l, r, c, t = dq.popleft()
#         for i in range(6):
#             nl = l + dl[i]
#             nr = r + dr[i]
#             nc = c + dc[i]
#             if isValid(nl, nr, nc) and building[nl][nr][nc] != "#":
#                 if building[nl][nr][nc] == "E":
#                     escaped = True
#                     break 
#                     # ⭐️ bfs에서의 queue는 무조건 t 순으로 정렬되어 있다.
#                         # 즉 앞으로 나올 것은 t가 더 많거나 적어도 같다
#                 else:
#                     dq.append((nl, nr, nc, t + 1))
#                     building[nl][nr][nc] = "#"
#     if escaped:
#         print(f"Escaped in {t + 1} minute(s).")
#     else:
#         print("Trapped!")




'''
# 사용해야 하는 알고리즘 = dfs 혹은 bfs (완전탐색)
    : 일정 높이 이상의 안전지대를 구하려면
    : 완전 탐색이 필요하다.

# 문제 풀이 아이디어
    : 각 비의 양에 따라서 물에 잠기는 곳을
    : 다른 지도문제의 벽이라고 생각하고
    : 각 비의 양에 따라서 dfs를 돌면서 최대 값을 구하면 된다.

# 의사 코드
    1. 입력을 받아서 인접 행렬로 만든다.
    2. dfs 함수를 짤 때 비의 높이를 받아서 비의 높이 이상만 방문하도록 짠다.
    3. 비의 높이를 0부터 시작해서 1씩 늘여가면서 반복문을 돈다.
        3-1. 인접 행렬의 [0][0]부터 완전 탐색을 돌면서
        3-2. 안전 지대의 갯수를 세고
        3-3. 기존의 max 갯수와 비교해서 최댓값을 갱신한다.
    4.  안전지대의 갯수가 0이면 반복문을 탈출한다. (다 잠김)
    5. 최댓값을 출력한다.

# 주의할 점!
    : 높이가 전부 같아서 한번도 안 잠기다가 한방에 다 잠기는 경우
    : 높이가 전부 1이여서 비를 1부터 시작하면 다 잠겨 버리는 경우

# 시간복잡도
    : 모든 좌표를 도는 반복문이 O(n**n)
    : 그리고 다 잠길 때 까지 반복문을 도는데 높이가 최대 100이므로 안전

'''
# import sys
# sys.setrecursionlimit(10000)

# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]

# n = int(input())
# board = [list(map(int, input().split())) for _ in range(n)]


# def isValid(x, y):
#     if x >= 0 and x < n and y >= 0 and y < n and check[y][x] == 0:
#         return True
#     else:
#         return False

# def dfs(x, y, rain):
#     global check
#     check[y][x] = 1
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if isValid(nx, ny) and board[ny][nx] > rain:
#             dfs(nx, ny, rain)

# rain = 0
# maxResult = 0

# while True:
#     check = [[0 for _ in range(n)] for _ in range(n)]
#     currentResult = 0
#     for i in range(n):
#         for j in range(n):
#             if board[j][i] > rain and check[j][i] == 0:
#                 dfs(i, j, rain)
#                 currentResult += 1
#     maxResult = max(maxResult, currentResult)
#     if currentResult < 1:
#         break
#     rain += 1

# print(maxResult)
