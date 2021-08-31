import sys
sys.stdin=open("input.txt", "r")

'''

'''
n = int(input())
board = [[0 for _ in range(n)] for _ in range(n)]

def isAble(x, y):
    if 1 in board[y]:
        return False
    for i in range(n):
        if 1 in board[i][x]:
            return False
    

'''
# 사용해야 하는 알고리즘 = 브루트 포스
    : 주어지는 수열에 일정 규칙은 없다
    : = 모든 케이스를 감안해야 한다.

# 문제 풀이 아이디어
    : combination을 활용해서 길이가 1 ~ n인 부분 수열을 구한다.
    : 부분 수열은 순서가 어차피 순서가 정해져 있으므로 combination

# 의사코드
    1. 입력을 받고 수열은 list에 저장한다.
    2. i가 1 ~ n까지 반복문을 돌린다.
        2-1. combination을 이용해서 수열의 길이 i인 조합을 구한다.
        2-2. 조합의 합이 s와 같으면 cnt += 1을 한다.
    3. cnt를 출력한다.
'''
# from itertools import combinations
# n, s = map(int, input().split())
# nums = list(map(int, input().split()))
# result = 0

# for i in range(1, n + 1):
#     combis = list(combinations(nums, i))
#     for combi in combis:
#         if sum(combi) == s:
#             result += 1

# print(result)


'''
# 사용해야 하는 알고리즘 = bfs
    : 
'''

# from collections import deque
# n, k = map(int, input().split())

# def bfs(n, k):
#     dq = deque()
#     dq.append(n)
#     ans = 0
#     while k > 0:
#         temp = deque()
#         visited = set()
#         while dq:
#             num = list(str(dq.popleft()))
#             for i in range(len(num) - 1):
#                 for j in range(i + 1, len(num)):
#                     num[i], num[j] = num[j], num[i]
#                     if num[0] == "0":
#                         num[i], num[j] = num[j], num[i]
#                         break
#                     result = int(''.join(num))
#                     if result not in visited:
#                         temp.append(result)
#                         visited.add(result)
#                     num[i], num[j] = num[j], num[i]
#         dq = temp
#         if not dq:
#             print(-1)
#             return
#         k -= 1

#     print(max(visited))
#     return

# bfs(n, k)

