# 로컬 환경에서 입력을 받기 위한 양식
import sys
sys.stdin=open("input.txt", "r")

# 수리공 항승

n, l = map(int, input().split())
holes = list(map(int, input().split()))

pipe = [False] * 1001

for hole in holes:
    pipe[hole] = True

cnt = 0
i = 0
while i < 1001:
    if pipe[i] == True:
        cnt += 1
        i += l
    else:
        i += 1

print(cnt)





# # 동전 0

# n, k = map(int, input().split())
# coins = [int(input()) for _ in range(n)]
# coins.sort(reverse=True)

# count = 0
# for coin in coins:
#     count += k // coin
#     k = k % coin

# print(count)
    

# # 사탕 게임
# '''
# 1. 사탕 바꾸기
# 2. 연속된 갯수 세기
# 3. 원상복구
# 4. 반복하면서 최댓값 구하기
# '''
# from itertools import groupby

# n = int(input())
# board = [list(input()) for _ in range(n)]
#     # 문자열 list 하면 한글자씩 리스트로 반환

# # 한줄의 최대 사탕 세는 함수
# def getMaxCandy(row):
#     maxCandy = 1
#     for val, group in groupby(row):
#         currentCandy = len(list(group))
#         maxCandy = max(currentCandy, maxCandy)
#     return maxCandy

# # 현재 보드에 있는 사탕을 세는 함수
# def countCandy(i, j):
#     maxCandy = 0
#     maxCandy = max(getMaxCandy(board[i]), maxCandy)
#     if i + 1 < len(board) - 1: 
#         maxCandy = max(getMaxCandy(board[i + 1]), maxCandy)
#     for a in range(2):
#         column = []
#         for b in range(len(board)):
#             if j + a < len(board) - 1:
#                 column.append(board[b][j + a])
#                 maxCandy = max(getMaxCandy(column), maxCandy)
#     return maxCandy    


# # 답 저장하는 전역변수
# ans = 0

# # i가 y좌표 j가 x좌표라고 생각
# for i in range(len(board)):
#     for j in range(len(board)):
#         # 오른쪽 사탕과 바꾸기
#         if j < (len(board) - 1):
#             board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
#             ans = max(countCandy(i, j), ans)
#             board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
#         # 아래쪽 사탕과 바꾸기
#         if i < (len(board) - 1):
#             board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
#             ans = max(countCandy(i, j), ans)
#             board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]

# print(ans)


# # 일곱 난쟁이

# h = [int(input()) for _ in range(9)]

# from itertools import combinations

# for combi in combinations(h, 7):
#     ans = list(combi)
#     if sum(ans) == 100:
#         ans.sort()
#         for i in ans:
#             print(i)
#         break

