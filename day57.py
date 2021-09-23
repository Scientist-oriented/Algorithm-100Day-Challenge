import sys
sys.stdin=open("input.txt", "r")

# 환승
from collections import deque

N, K, M = map(int, input().split())
adj = [[] for _ in range(N + M)]
    # 0 ~ N - 1은 도시, N ~ N + M - 1은 하이퍼 튜브

for i in range(M):
    stations = list(map(int, input().split()))
    for station in stations:
        adj[N + i].append(station - 1)
        adj[station - 1].append(N + i)

def bfs(x):
    dq = deque()
    visited = [False for _ in range(N + M)]

    dq.append((x, 0))
    visited[x] = True

    while dq:
        node, cost = dq.popleft()
        if node == N - 1:
            return cost + 1
        for next in adj[node]:
            if not visited[next]:
                if next < N:
                    dq.append((next, cost + 1))
                else:
                    dq.append((next, cost))
                visited[next] = True
    return -1

print(bfs(0))




# # 공통 부분 문자열
# s1 = input()
# s2 = input()
# dp = [[0 for _ in range(len(s2))] for _ in range(len(s1))]

# for r in range(len(s1)):
#     for c in range(len(s2)):
#         if s1[r] == s2[c]:
#             dp[r][c] = dp[r - 1][c - 1] + 1 if r - 1 >= 0 and c - 1 >= 0 else 1

# print(max(max(line) for line in dp))

# # 용돈 관리
# N, M = map(int, input().split())
# spendings = []
# for _ in range(N):
#     spendings.append(int(input()))

# s = max(spendings)
# e = sum(spendings)
# ans = N

# while s <= e:
#     mid = (s + e) // 2
#     money = 0
#     cnt = 0
#     for spending in spendings:
#         if spending > money:
#             money = mid - spending
#             cnt += 1
#         else:
#             money -= spending
#     if cnt > M:
#         s = mid + 1
#     else:
#         e = mid - 1

# print(mid)



# # 이동하기
# N, M = map(int, input().split())
# board = []
# for _ in range(N):
#     board.append(list(map(int, input().split())))

# dp = [[0 for _ in range(M)] for _ in range(N)]

# for r in range(N):
#     for c in range(M):
#         if r - 1 >= 0 and c - 1 >= 0:
#             dp[r][c] = max(dp[r - 1][c], dp[r][c - 1]) + board[r][c]
#         elif r - 1 < 0:
#             dp[r][c] = dp[r][c - 1] + board[r][c]
#         elif c - 1 < 0:
#             dp[r][c] = dp[r - 1][c] + board[r][c]
#         else:
#             dp[r][c] = board[r][c]

# print(dp[N - 1][M - 1])


# # 로또
# from itertools import combinations

# def printLottoNums(nums):
#     for combi in combinations(nums, 6):
#         for num in combi:
#             print(num, end=" ")
#         print()

# cnt = 0

# while True:
#     k, *nums = map(int, input().split())
#     if k == 0:
#         break
#     if cnt > 0:
#         print()
#     printLottoNums(list(nums))
#     cnt += 1


# # 결혼식
# from collections import deque

# n = int(input())
# m = int(input())

# adj = [[] for _ in range(n)]

# for _ in range(m):
#     a, b = map(lambda x: int(x) - 1, input().split())
#     adj[a].append(b)
#     adj[b].append(a)

# def bfs(x):
#     dq = deque()
#     visited = [False for _ in range(n)]
    
#     dq.append((x, 0))
#     cnt = 0

#     while dq:
#         node, cost = dq.popleft()
#         if cost <= 2:
#             cnt += 1
#             visited[node] = True
#             for friend in adj[node]:
#                 if not visited[friend]:
#                     dq.append((friend, cost + 1))
#                     visited[friend] = True

#     return cnt - 1

# print(bfs(0))
