import sys
sys.stdin=open("input.txt", "r")

# n = int(input())
# cache = [-1] * (n + 1)
# cache[0] = 0
# cache[1] = 1

# for i in range(n + 1):
#     if cache[i] < 0:
#         cache[i] = cache[i - 1] + cache[i - 2]

# print(cache[n])

# n, k = map(int, input().split())

# # ✅ cache 공간 만들기
# board = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

# # ✅ 초깃값 넣기
# board[1][0] = board[1][1] = 1

# # ✅ 점화식에 따라 데이터 넣기
# for i in range(2, n + 1):
#     for j in range(n + 1):
#         board[i][j] = board[i - 1][j - 1] + board[i - 1][j]

# print(board[n][k] % 10007)

# n = int(input())
# mod = 10007

# cache = [-1] * (n + 1)

# for i in range(1, n + 1):
#     if i == 1:
#         cache[i] = 1
#         continue
#     elif i == 2:
#         cache[i] = 2
#         continue
#     cache[i] = (cache[i - 1] + cache[i - 2]) 

# print(cache[n] % mod)

# T = int(input())

# for _ in range(T):
#     n = int(input())
#     stickers = []
#     for _ in range(2):
#         stickers.append(list(map(int, input().split())))
#     cache = [[0 for _ in range(n)] for _ in range(2)]
#     for i in range(n):
#         if i == 0:
#             cache[0][i] = stickers[0][i]
#             cache[1][i] = stickers[1][i]
#         elif i == 1:
#             cache[0][i] = cache[1][i - 1] + stickers[0][i]
#             cache[1][i] = cache[0][i - 1] + stickers[1][i]
#         else:
#             cache[0][i] = max(cache[1][i - 2], cache[1][i - 1]) + stickers[0][i]
#             cache[1][i] = max(cache[0][i - 2], cache[0][i - 1]) + stickers[1][i]
#     print(max(cache[0][n - 1], cache[1][n - 1]))

n = int(input())
mod = 1000000000
cache = [[0 for _ in range(10)] for _ in range(n + 1)]

for i in range(1, n + 1):
    if i == 1:
        for j in range(1, 10):
            cache[i][j] = 1
    else:
        for j in range(0, 10):
            if j == 0:
                cache[i][j] = cache[i - 1][j + 1]
            elif j == 9:
                cache[i][j] = cache[i - 1][j - 1]
            else:
                cache[i][j] = cache[i - 1][j + 1] + cache[i - 1][j - 1]

print(sum(cache[n]) % mod)



