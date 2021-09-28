import sys
sys.stdin=open("input.txt", "r")

# 바이러스
N = int(input())
M = int(input())
connection = [[] for _ in range(N + 1)]
for _ in range(M):
    c1, c2 = map(int, input().split())
    connection[c1].append(c2)
    connection[c2].append(c1)

def dfs(c):
    stack = []
    cnt = 0
    visited = [False for _ in range(N + 1)]

    stack.append(c)
    visited[c] = True

    while stack:
        c1= stack.pop()
        for c2 in connection[c1]:
            if not visited[c2]:
                stack.append(c2)
                visited[c2] = True
                cnt += 1

    return cnt

print(dfs(1))
    


# # 주사위 윷놀이

# # 바로 다음 칸이 어디인지 알려주는 nextStop
# nextStop = [0 for _ in range(33)]
# for i in range(21):
#     nextStop[i] = i + 1
# nextStop[21] = 21
# nextStop[22], nextStop[23], nextStop[24] = 23, 24, 30
# nextStop[25], nextStop[26] = 26, 30
# nextStop[27], nextStop[28], nextStop[29] = 28, 29, 30
# nextStop[30], nextStop[31], nextStop[32] = 31, 32, 20

# # 칸의 점수를 알려주는 board
# board = [0 for _ in range(33)]
# for i in range(1, 21):
#     board[i] = i * 2
# board[22], board[23], board[24] = 13, 16, 19
# board[25], board[26] = 22, 24
# board[27], board[28], board[29] = 28, 27, 26
# board[30], board[31], board[32] = 25, 30, 35

# # 파란 화살표를 탈 경우 어디로 갈지 알려주는 blue
# blue = [0 for _ in range(16)]
# blue[5], blue[10], blue[15] = 22, 25, 27

# # 주사위 눈금을 보고 어디로 갈지 정해준다.
# def getNextStop(position, diceNum):
#     # blue 눈금에 있는 경우를 고려해야 한다.
#         # 일단 1칸 이동하고 dice에서 하나 빼는 걸로
#     if position == 5:
#         position = blue[5]
#         diceNum -= 1
#     elif position == 10:
#         position = blue[10]
#         diceNum -= 1
#     elif position == 15:
#         position = blue[15]
#         diceNum -= 1

#     for _ in range(diceNum):
#         position = nextStop[position]
#     return position

# def dfs(turn, score):
#     global ans
#     if turn == 10:
#         ans = max(ans, score)
#         return

#     # 말 4개를 해당 주사위만큼 이동하는 모든 경우를 dfs
#     for i in range(4):
#         now = markers[i]
#         diceNum = dice[turn]
#         next = getNextStop(now, diceNum)

#         # 도착지가 아닌데 이미 말이 있는 경우 -> 갈 수 없음
#         if visited[next] and next != 21:
#             continue

#         visited[now], visited[next], markers[i] = False, True, next
#         dfs(turn + 1, score + board[next])
#         visited[now], visited[next], markers[i] = True, False, now

# markers = [0 for _ in range(4)]
# visited = [0 for _ in range(33)]
# dice = list(map(int, input().split()))

# ans = 0
# dfs(0, 0)
# print(ans)

# # 보물섬
# from collections import deque

# dr = [1, -1, 0, 0]
# dc = [0, 0, 1, -1]

# def isPossible(r, c):
#     if r < 0 or r > N - 1:
#         return False
#     elif c < 0 or c > M - 1:
#         return False
#     else:
#         return True

# def bfs(r, c):
#     dq = deque()
#     visited = [[False for _ in range(M)] for _ in range(N)]

#     dq.append((r, c, 0))
#     visited[r][c] = True

#     while dq:
#         r, c, cost = dq.popleft()
#         for i in range(4):
#             nr = r + dr[i]
#             nc = c + dc[i]
#             if isPossible(nr, nc) and board[nr][nc] == "L" and not visited[nr][nc]:
#                 dq.append((nr, nc, cost + 1))
#                 visited[nr][nc] = True
#     return cost

# N, M = map(int, input().split())
# board = []
# for _ in range(N):
#     board.append(list(input()))

# ans = 0

# for r in range(N):
#     for c in range(M):
#         if board[r][c] == "L":
#             ans = max(bfs(r, c), ans)

# print(ans)




    

# # 그리고 하나가 남았다.
# from collections import deque

# '''
# 남은돌 8 -> 7 -> 6 -> 5
# idx 2 -> 6 -> 4 -> 3
# next idx = current idx + (k - 1) - (현재남은돌 if 크면)
# '''

# def getNextIdx(leftStones, currentIdx, k):
#     # print(f"leftStones = {leftStones}, currentIdx: {currentIdx}")
#     nextIdx = currentIdx + (k - 1)
#     if nextIdx > leftStones - 1:
#         return nextIdx % leftStones
#     else:
#         return nextIdx

# def solve(n, k, m):
#     stones = [i for i in range(1, n + 1)]
#     currentIdx = m - 1
#     while len(stones) > 1:
#         del stones[currentIdx]
#         currentIdx = getNextIdx(len(stones), currentIdx, k)
#     print(stones[0])

# while True:
#     n, k, m = map(int, input().split())
#     if n + k + m == 0:
#         break
#     solve(n, k, m)

# # 랜선 자르기
# K, N = map(int,input().split())
# lines = []
# for _ in range(K):
#     lines.append(int(input()))

# s = 1
# e = max(lines)
# ans = 0

# while s <= e:
#     mid = (s + e) // 2
#     result = 0
#     for line in lines:
#         result += line // mid
#     if result >= N:
#         ans = mid
#         s = mid + 1
#     else:
#         e = mid - 1

# print(ans)



# # 원판 돌리기
# from collections import deque
# N, M, T = map(int, input().split())
# circles = [deque([0] * M)]
# for _ in range(N):
#     circles.append(deque(map(int, input().split())))
# circles.append(deque([0] * M))

# def prettyPrint():
#     for i in range(1, N + 1):
#         print(circles[i])
#     print()

# def rotate(x, d, k):
#     for i in range(x, N + 1, x):
#         if d == 0:
#             for _ in range(k):
#                 circles[i].appendleft(circles[i].pop()) 
#         else:
#             for _ in range(k):
#                 circles[i].append(circles[i].popleft())

# def findSame():
#     sameCoords = set()
#     for i in range(1, N + 1):
#         for j in range(M):
#             if circles[i][j] == circles[i][j - 1] != 0:
#                 sameCoords.add((i, j))
#                 sameCoords.add((i, j - 1))
#             if j + 1 < M - 1 and circles[i][j] == circles[i][j + 1] != 0:
#                 sameCoords.add((i, j))
#                 sameCoords.add((i, j + 1))
#             if circles[i][j] == circles[i - 1][j] != 0:
#                 sameCoords.add((i, j))
#                 sameCoords.add((i - 1, j))
#             if circles[i][j] == circles[i + 1][j] != 0:
#                 sameCoords.add((i, j))
#                 sameCoords.add((i + 1, j))
#     return list(sameCoords)

# def deleteSame(sameCoords):
#     for coord in sameCoords:
#         i, j = coord
#         circles[i][j] = 0

# def getTotal():
#     result = 0
#     for i in range(1, N + 1):
#         for j in range(M):
#             result += circles[i][j]
#     return result

# def getNumOfNums():
#     result = 0
#     for i in range(1, N + 1):
#         for j in range(M):
#             if circles[i][j] > 0:
#                 result += 1
#     return result 

# def noSameOperation():
#     if getNumOfNums() == 0:
#         return
#     avg = getTotal() / getNumOfNums()
#     for i in range(1, N + 1):
#         for j in range(M):
#             if circles[i][j] == 0:
#                 continue
#             elif circles[i][j] > avg:
#                 circles[i][j] -= 1
#             elif circles[i][j] < avg:
#                 circles[i][j] += 1

# for _ in range(T):
#     x, d, k = map(int, input().split())
#     rotate(x, d, k)
#     sameCoords = findSame()
#     #prettyPrint()
#     if sameCoords:
#         deleteSame(sameCoords)
#     else:
#         #prettyPrint()
#         noSameOperation()

# print(getTotal())
# #prettyPrint()





# # 리모컨
# N = int(input())
# M = int(input())
# if M > 0:
#     brokenButtons = list(input().split())
# else:
#     brokenButtons = []

# def isPossibleByButtons(channel):
#     if channel < 0:
#         return False
#     channel = str(channel)
#     for button in brokenButtons:
#         if button in channel:
#             return False
#     return True

# def getChannelCost(channel):
#     return len(str(channel)) + abs(N - channel)

# ans = abs(N - 100)

# for channel in range(1000000):
#     if isPossibleByButtons(channel):
#         cost = getChannelCost(channel)
#         ans = min(cost, ans)

# print(ans)
# upper = N
# lower = N
# cnt = 0
# fromHundred = abs(N - 100)

# if N == 100:
#     print(0)
# elif len(brokenButtons) == 10:
#     print(fromHundred)
# else:
#     while True:
#         upper += 1
#         lower -= 1
#         if isPossibleByButtons(upper) or isPossibleByButtons(lower):
#             if isPossibleByButtons(upper) and isPossibleByButtons(lower):
#                 # 동시에 되는 경우 upper와 lower의 길이가 다를 수 있기 때문
#                 print(min(fromHundred, len(str(upper)) + (upper - N), len(str(lower)) + (N - lower)))
#                 break
#             elif isPossibleByButtons(upper):
#                 print(min(fromHundred, len(str(upper)) + (upper - N)))
#                 break
#             else:
#                 print(min(fromHundred, len(str(lower)) + (N - lower)))
#                 break
