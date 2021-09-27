import sys
sys.stdin=open("input.txt", "r")

# 리모컨

        
# # 욕심쟁이 판다
# # n = int(input())
# # board = []
# # for _ in range(n):
# #     board.append(list(map(int, input().split())))

# # dr = [1, -1, 0, 0]
# # dc = [0, 0, 1, -1]

# # def isPossible(r, c):
# #     if r < 0 or r > n - 1:
# #         return False
# #     elif c < 0 or c > n - 1:
# #         return False
# #     else:
# #         return True

# # def dfs(r, c, cnt):
# #     global ans
# #     moved = False
# #     bamboo = board[r][c]
# #     for i in range(4):
# #         nr = r +dr[i]
# #         nc = c +dc[i]
# #         if isPossible(nr, nc) and board[nr][nc] > bamboo:
# #             board[r][c] = 0
# #             dfs(nr, nc, cnt + 1)
# #             moved = True
# #             board[r][c] = bamboo
# #     if not moved:
# #         ans = max(cnt, ans)
        
# # ans = 0
# # for r in range(n):
# #     for c in range(n):
# #         dp = [[0 for _ in range(n)] for _ in range(n)]
# #         dfs(r, c, 1)
# # print(ans)

# import sys
# sys.setrecursionlimit(10**9)

# # 입력 받기
# n = int(input())
# board = []
# for _ in range(n):
#     board.append(list(map(int, input().split())))

# dr = [1, -1, 0, 0]
# dc = [0, 0, 1, -1]

# def isPossible(r, c):
#     if r < 0 or r > n - 1:
#         return False
#     elif c < 0 or c > n - 1:
#         return False
#     else:
#         return True

# #💡 visited에 저장하는 것은 현재 칸에서 멈출 경우 최대 이동경로이다.
# visited = [[0 for _ in range(n)] for _ in range(n)]

# #💡 dfs를 통해서 탐색하는 것은 현재 칸의 이전칸이 될 수 있는 것이다. (역방향 탐색)
#     # 블로그 코드는 정방향 탐색을 했는데 이게 더 자연스러운 것 같다.
# def dfs(r, c):
#     if visited[r][c] < 1:
#         visited[r][c] = 1 # 주변에 갈 수 있는 곳이 없는 경우 1이 저장된다.
#         for i in range(4):
#             nr = r + dr[i]
#             nc = c + dc[i]
#             if isPossible(nr, nc) and board[nr][nc] < board[r][c]:
#                     # 현재 칸으로 올 수 있는 칸을 찾고 있으므로 현재칸 보다 나무가 적은 칸을 찾는다.
#                 visited[r][c] = max(dfs(nr, nc) + 1, visited[r][c])
#                     # dfs의 결과 (= 현재칸까지의 최대 칸수)과 이미 저장된 현재칸까지의 최대 칸수를 비교한다.
#     return visited[r][c]

# ans = 0
# for r in range(n):
#     for c in range(n):
#         ans = max(ans, dfs(r, c))
# print(ans)



# # 빙산
# N, M = map(int, input().split())
# board = []
# for _ in range(N):
#     board.append(list(map(int, input().split())))

# dr = [1, -1, 0, 0]
# dc = [0, 0, 1, -1]

# def printPretty():
#     for i in range(N):
#         print(board[i])
#     print()
    
# def getMeltHeight():
#     melt = [[0 for _ in range(M)] for _ in range(N)]
#     for r in range(N):
#         for c in range(M):
#             if board[r][c] != 0:
#                 for i in range(4):
#                     nr = r + dr[i]
#                     nc = c + dc[i]
#                     if board[nr][nc] == 0:
#                         melt[r][c] += 1
#     return melt

# def reflectMelt(melt):
#     for r in range(N):
#         for c in range(M):
#             if melt[r][c] > 0:
#                 board[r][c] -= melt[r][c]
#                 if board[r][c] < 0:
#                     board[r][c] = 0

# def getConnected():
#     result = 0
#     visited = [[False for _ in range(M)] for _ in range(N)]

#     for r in range(N):
#         for c in range(M):
#             if board[r][c] > 0 and not visited[r][c]:
#                 visited = dfs(r, c, visited)
#                 result += 1
#     return result

# def dfs(r, c, visited):
#     stack = []
#     stack.append((r, c))
#     visited[r][c] = True

#     while stack:
#         r, c = stack.pop()
#         for i in range(4):
#             nr = r + dr[i]
#             nc = c + dc[i]
#             if board[nr][nc] > 0 and not visited[nr][nc]:
#                 stack.append((nr, nc))
#                 visited[nr][nc] = True

#     return visited

# def isFinished():
#     for r in range(N):
#         for c in range(M):
#             if board[r][c] != 0:
#                 return False
#     return True

# ans = 0

# while True:
#     if isFinished():
#         print(0)
#         break

#     connected = getConnected()
#     if connected > 1:
#         print(ans)
#         break

#     melt = getMeltHeight()
#     reflectMelt(melt)
#     ans += 1