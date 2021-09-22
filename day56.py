import sys
sys.stdin=open("input.txt", "r")



# # 파이프 옮기기
# '''
# pipe: 위치 (파이프가 끝나는 지점) + 모양
# 모양:
#     0 = 가로
#     1 = 세로
#     2 = 대각선
# '''

# def isHorizontalPossible(r, c):
#     if c + 1 > N - 1:
#         return False
#     if board[r][c + 1] == 1:
#         return False
#     return True

# def isVerticalPossible(r, c):
#     if r + 1 > N - 1:
#         return False
#     if board[r + 1][c] == 1:
#         return False
#     return True

# def isDiagonalPossible(r, c):
#     if r + 1 > N - 1 or c + 1 > N - 1:
#         return False
#     if board[r + 1][c] == 1 or board[r][c + 1] == 1 or board[r + 1][c + 1] == 1:
#         return False
#     return True

# def dfs(r, c, pos):
#     global cnt
#     if r == N - 1 and c == N - 1:
#         cnt += 1
#         return

#     if pos == 0:
#         if isHorizontalPossible(r, c):
#             dfs(r, c + 1, 0)
#         if isDiagonalPossible(r, c):
#             dfs(r + 1, c + 1, 2)
#     elif pos == 1:
#         if isVerticalPossible(r, c):
#             dfs(r + 1, c, 1)
#         if isDiagonalPossible(r, c):
#             dfs(r + 1, c + 1, 2)
#     else:
#         if isHorizontalPossible(r, c):
#             dfs(r, c + 1, 0)
#         if isVerticalPossible(r, c):
#             dfs(r + 1, c, 1)
#         if isDiagonalPossible(r, c):
#             dfs(r + 1, c + 1, 2)

# N = int(input())
# board = []
# for _ in range(N):
#     board.append(list(map(int, input().split())))
# cnt = 0

# dfs(0, 1, 0)
# print(cnt)

# # 드래곤 커브
# def rotateClockwise(d):
#     return d + 1 if d != 3 else 0

# def initiateCurve(x, y, d):
#     return [(x, y, d)]

# def getEndPoint(line):
#     x, y, d = line
#     if d == 0:
#         return x + 1, y
#     elif d == 1:
#         return x, y - 1
#     elif d == 2:
#         return x - 1, y
#     else:
#         return x, y + 1

# # 앞으로 그려야할 방향들을 모은 리스트 (d만 들어있음)
#     # 드래곤 커브들의 방향만 모아서 회전시키고 역순으로 담았음.
# def getToDrawList(curve: list):
#     return list(map(lambda x: rotateClockwise(x[2]), reversed(curve)))

# # 다음 세대의 드래곤 커브를 그려준다.
# def getNextGeneration(curve: list):
#     toDrawList = getToDrawList(curve)
#     for d in toDrawList:
#         x, y = getEndPoint(curve[-1])
#         curve.append((x, y, d))
#     return curve
    
# def bringCurveOnBoard(curve):
#     coords = list(map(lambda x: (x[0], x[1]), curve))
#     lastCoord = getEndPoint(curve[-1])
#     coords.append(lastCoord)
#     for coord in coords:
#         x, y = coord
#         board[y][x] = 1

# def getCurve(x, y, d, g):
#     curve = initiateCurve(x, y, d)
#     for _ in range(g):
#         curve = getNextGeneration(curve)
#     return curve

# board = [[0 for _ in range(101)] for _ in range(101)]

# N = int(input())
# for _ in range(N):
#     x, y, d, g = map(int, input().split())
#     curve = getCurve(x, y, d, g)
#     bringCurveOnBoard(curve)

# ans = 0
# for r in range(101):
#     for c in range(101):
#         if board[r][c] == 1:
#             if r + 1 <= 100 and c + 1 <= 100:
#                 if board[r + 1][c] == 1 and board[r][c + 1] == 1 and board[r + 1][c + 1] == 1:
#                     ans += 1
# print(ans)





# # 아기 상어
# from collections import deque

# def isValid(r, c):
#     if r < 0 or r > N - 1:
#         return False
#     elif c < 0 or c > N - 1:
#         return False
#     elif board[r][c] > shark[2]:
#         return False
#     else:
#         return True

# def getDistance(R, C):
#     dq = deque()
#     visited = [[False for _ in range(N)] for _ in range(N)]

#     sr, sc = shark[0], shark[1]
#     dq.append((sr, sc, 0))
#     visited[sr][sc] = True

#     while dq:
#         r, c, d = dq.popleft()
#         if r == R and c == C:
#             return d
#         for i in range(4):
#             nr = r + dr[i]
#             nc = c + dc[i]
#             if isValid(nr, nc) and not visited[nr][nc]:
#                 dq.append((nr, nc, d + 1))
#                 visited[nr][nc] = True
#     return False # 갈 수 없으면 False 반환

# def findFoods():
#     foods = []
#     size = shark[2]
#     for r in range(N):
#         for c in range(N):
#             if 0 < board[r][c] < size:
#                 distance = getDistance(r, c)
#                 if distance: # 
#                     foods.append((r, c, distance))  
#     return foods

# def pickFood(foods: list):
#     foods.sort(key = lambda x: (x[2], x[0], x[1]))
#     return foods[0]

# def moveAndEat(food):
#     global time, shark
#     r, c, d = food
#     time += d
#     board[r][c] = 0
    
#     if shark[2] > shark[3] + 1:
#         shark = (r, c, shark[2], shark[3] + 1)
#     else:
#         shark = (r, c, shark[2] + 1, 0)

# dr = [1, -1, 0, 0]
# dc = [0, 0, 1, -1]

# N = int(input())
# board = []
# for _ in range(N):
#     board.append(list(map(int, input().split())))

# for r in range(N):
#     for c in range(N):
#         if board[r][c] == 9:
#             shark = (r, c, 2, 0)
#             board[r][c] = 0 # 상어는 좌표를 저장해서 관리할 것임 (안지우면 길막함)
#             break

# time = 0

# while True:
#     foods = findFoods()
#     #print(f"shark: {shark} time:{time} foods: {foods}")
#     if not foods: # 먹을게 없으면 종료
#         break
#     food = pickFood(foods)
#     moveAndEat(food)

# print(time)

# # 인구이동
# dr = [1, -1, 0, 0]
# dc = [0, 0, 1, -1]

# def isConnected(r, c, nr, nc):
#     diff = abs(board[r][c] - board[nr][nc])
#     if diff >= L and diff <= R:
#         return True
#     else:
#         return False

# def isValid(r, c):
#     if r < 0 or r > N - 1:
#         return False
#     elif c < 0 or c > N - 1:
#         return False
#     else:
#         return True

# def dfs(r, c, visited):
#     result = []
#     result.append((r, c))
#     stack = []
#     stack.append((r, c))
#     visited[r][c] = True
#     while stack:
#         r, c = stack.pop()
#         for i in range(4):
#             nr = r + dr[i]
#             nc = c + dc[i]
#             if isValid(nr, nc) and not visited[nr][nc] and isConnected(r, c, nr, nc):
#                 result.append((nr, nc))
#                 stack.append((nr, nc))
#                 visited[nr][nc] = True
#     return result, visited

# def getConfeds():
#     confeds = []
#     visited = [[False for _ in range(N)] for _ in range(N)]
#     for r in range(N):
#         for c in range(N):
#             if not visited[r][c]:
#                 confed, visited = dfs(r, c, visited)
#                 confeds.append(confed)
#     return confeds

# def getConfedAvg(confed):
#     total = 0
#     for r, c in confed:
#         total += board[r][c]
#     return round(total / len(confed))
    
# def movePeo(confeds):
#     flag = False # 연합은 되는데 인구이동은 안 일어나는 경우
#     for confed in confeds:
#         avg = getConfedAvg(confed)
#         for r, c in confed:
#             if board[r][c] != avg:
#                 board[r][c] = avg
#                 flag = True
#     return flag

# def isMoveFinished(confeds):
#     if len(confeds) == N ** 2:
#         return True
#     else:
#         return False

# def printPretty():
#     for i in range(N):
#         print(board[i])
#     print()

# N, L, R = map(int, input().split())
# board = []
# for _ in range(N):
#     board.append(list(map(int, input().split())))
# ans = 0

# while True:
#     confeds = getConfeds()
#     if not isMoveFinished(confeds):
#         if movePeo(confeds):
#             ans += 1
#         else:
#             break
#     else:
#         break

# print(ans)