import sys
sys.stdin=open("input.txt", "r")

'''
# 4주차 퀴즈 n-queen 문제
# 사용해야 하는 알고리즘 = dfs, 백트래킹
    : dfs를 사용해서 각 행마다 놓을 수 있는 퀸의 열을 완전탐색

# 문제 풀이 아이디어
    : 퀸이 각 1행에 1개만 놓을 수 있기 때문에 이차원 배열이 아니라
    : 일반 배열을 사용해서 visited 체크를 한다.

# 의사코드
    1. 퀸이 놓인 행을 표시하기 위해 N 길이의 배열을 선언하고 답을 저장할 result = 0을 선언한다.
    2. 현재 퀸을 놓을 행의 index번호를 인자로 받는 dfs 함수를 선언한다.
        2-1. 현재 퀸을 놓을 index가 N이면 (= 퀸을 다 놓음) result += 1을 하고 리턴한다.
        2-2. 현재 행의 각열에 퀸을 놓는 방식으로 반복문을 돌린다.
            2-2-1. 퀸을 놓고 나서 열 / 대각선에 겹치는 퀸이 없는지 확인한다.
            2-2-2. 겹치는 퀸이 없다면 다음 행의 dfs를 실시한다.
    3. result를 출력한다.
'''

from collections import deque
# 미로 탐색
N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def bfs(r, c):
    dq = deque()
    visited = [[0 for _ in range(M)] for _ in range(N)]
    dq.append((r, c))
    visited[r][c] = 1

    while dq:
        r, c = dq.popleft()
        if r == N - 1 and c == M - 1:
            print(visited[r][c])
            return
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and board[nr][nc] == "1" and visited[nr][nc] == 0:
                dq.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1

bfs(0, 0)




'''
# 사용하는 알고리즘 = bfs
    : bfs를 단계별로 실시해서 푸는 문제이다.
    : 큐에 바로 넣지 않고 temp에 넣어두었다가
    : 한단계가 끝나면 다시 큐로 옮겨서 bfs를 하면 된다.

# 문제 풀이 아이디어
    : 숫자를 문자로 바꾸고 list로 바꾸는 것이 좋다.
        : 첫 글자가 "0"일 때를 걸러내야 하기 때문에

# 의사 코드
    1. 입력을 받고 조합을 활용해서 i, j의 조합을 미리 만들어 놓는다.
    2. 큐에 첫번째 수를 넣고 bfs를 통해서 i, j의 조합을 완전 탐색한다.
        2-1. 각 단계별로 동일한 숫자가 나오면 queue에 넣을 필요가 없으므로 집합을 통해 걸러낸다.
        2-2. append할 숫자가 나오면 바로 큐에 넣지 않고 temp에 넣는다.
        2-3. 한단계가 지나면 k -= 1하고 temp를 큐로 옮기고 다시 실시한다.
    3. k = 0이 되면 큐에 있는 수 중에 가장 큰 수를 출력한다.
'''

'''
# 사용하는 알고리즘 = dfs, 백트래킹
    : dfs를 통해 최대한 큰것부터 붙이는 것으로 탐색을 하고
    : 붙이는게 안되면 백트래킹

# 문제 풀이 아이디어
    : 큰 색종이부터 붙이면 나중에 큰거 필요할 때 문제 발생!
    : 첫 1을 찾으면 거기서 부터 모든 색종이를 붙여본다는 생각으로 구현

# 의사코드
    1. 입력을 받고 남은 색종이 갯수를 표시하는 배열을 선언한다.
    2. 0, 0에서 반복문을 돌면서 1을 만나면 남은 색종이 크기 별로 완전탐색을 실시한다.
    3. 붙일 수 있으면 붙인 다음에 다음 1까지 완전탐색 해본다.
    4. 마지막에 도달하면 붙인 색종이 갯수를 배열에 저장
    5. 배열의 최솟값을 출력한다.
'''

'''
# 사용하는 알고리즘 = dfs, 백트래킹
    : dfs를 통해 동서남북 완전탐색을 하고 
    : 더 이상 갈 수 없다면 백트래킹

# 문제 풀이 아이디어
    : 한칸 더 갈 때마다 칸수를 저장하고
    : dfs를 한번 할 때마다 최댓값과 비교해서 global 변수에 저장하면 될 것 같다.

# 의사코드
    1. 입력을 받고 결과를 저장하기 위한 변수 (=0)을 설정한다.
    2. 아스키 코드를 활용해서 알파벳 방문 여부를 체크할 배열을 선언한다.
    3. 시작좌표와 칸수(=1) dfs를 실시한다.
        3-1. 매번 dfs에 진입하면 결과의 최댓값을 갱신한다.
        3-2. 동서남북 완전탐색을 통해서 가능한 위치에서 다시 dfs를 실시한다.
    4. 최종 결과를 출력한다.
'''

# import sys
# input = sys.stdin.readline

# R, C = map(int, input().split())
# board = [list(map(lambda x: ord(x) - 65, input().rstrip())) for _ in range(R)]

# dr = [1, -1, 0, 0]
# dc = [0, 0, 1, -1]


# result = 0
# alpha = [False] * 26

# def dfs(r, c, steps):
#     global result
#     result = max(result, steps)

#     for i in range(4):
#         nr = r + dr[i]
#         nc = c + dc[i]

#         if 0 <= nr < R and 0 <= nc < C and not alpha[board[nr][nc]]:
#             alpha[board[nr][nc]] = True
#             dfs(nr, nc, steps + 1)
#             alpha[board[nr][nc]] = False

# alpha[board[0][0]] = True
# dfs(0, 0, 1)
# print(result)




'''
# 사용하는 알고리즘 = dfs, 백트래킹
    : 첫 빈칸부터 가능한 모든 경우에 대해 dfs로 완전탐색
    : 중간에 안되는 경우에는 백트래킹 한다.

# 문제 풀이 아이디어
    : 딱 하나의 경우만 찾으면 되므로 n-queen처럼 cnt를 셀 필요는 없고
    : 재귀함수 도중에 조건을 만족하는 경우에 출력만 하면 된다.

# 의사코드
    1. 특정 좌표에 가능한 모든 수를 구하는 함수를 만든다.
        1-1. 1 ~ 9의 숫자를 가진 집합에서
        1-2. 같은 행 / 같은 열 / 같은 3*3에 있는 수를 빼고
        1-3. 리턴한다.
    2. 입력을 받고 0인 곳의 좌표를 리스트에 저장한다.
    3. dfs 안에서 빈칸 좌표를 가진 리스트를 돌면서 반복문을 실시한다.
        3-1. 마지막 인덱스를 통과했다면 현재 board를 출력한다.
        3-2. 현재 빈칸좌표에 대해서 가능한 수를 구한후
        3-3. 그 수를 빈칸에 넣고 다음 빈칸에 대해 dfs를 실시한다.
'''
# import sys
# board = [list(map(int, input().split())) for _ in range(9)]
# holes = [(r, c) for r in range(9) for c in range(9) if board[r][c] == 0]

# # 👉 가능한 수를 구해서 거기서 반복문! (넣고 따지는 것도 간단!)
# def getPossibles(r, c):
#     possibles = set(range(1, 10))
    
#     row = set(board[r])
#     column = set([board[i][c] for i in range(9)])
#     square = set([board[r1][c1] for r1 in range(r//3 * 3, r//3 * 3 + 3) for c1 in range(c//3 * 3, c//3 * 3 + 3)])

#     possibles = possibles - row - column - square
#     return list(possibles)

# def solve(i):
#     if i == len(holes):
#         # ✅ 이런 방식으로 리스트를 큐와 같은 방식으로 사용가능
#         for r in range(9):
#             for c in range(9):
#                 print(board[r][c], end=" ")
#             print()
#         sys.exit()

#     r, c = holes[i]
#     possibles = getPossibles(r, c)
#     for num in possibles:
#         board[r][c] = num
#         solve(i + 1)
#         board[r][c] = 0

# solve(0)



# import copy
# board = [list(map(int, input().split())) for _ in range(9)]
# stack = []
# for r in range(9):
#     for c in range(9):
#         if board[r][c] == 0:
#             stack.append((r, c))
# stack.reverse()

# def isValid(board, now):
#     nowR = now[0]
#     nowC = now[1]
#     nowValue = board[nowR][nowC]

#     row = copy.deepcopy(board[nowR])
#     column = [board[i][nowC] for i in range(9)] 
#     square = []

#     if nowR < 3:
#         rowRange = range(0, 3)
#     elif nowR < 6:
#         rowRange = range(3, 6)
#     else:
#         rowRange = range(6, 9)

#     if nowC < 3:
#         colRange = range(0, 3)
#     elif nowC < 6:
#         colRange = range(3, 6)
#     else:
#         colRange = range(6, 9)

#     for r in rowRange:
#         for c in colRange:
#             square.append(board[r][c])

#     row.remove(nowValue)
#     column.remove(nowValue)
#     square.remove(nowValue)

#     if (nowValue in row) or (nowValue in column) or (nowValue in square):
#         return False
#     else:
#         return True

# results = []

# def dfs(board, stack: list):
#     if not stack:
#         results.append(copy.deepcopy(board))
#         return
        
#     # 재귀함수로 dfs할 때는 바로 리턴하면 안되고 외부변수에 저장하고 한다.
#         # 대부분의 경우에 값을 바로 받으려고 하는 것은 위험하다!

#     board1 = copy.deepcopy(board)
#     now = stack.pop()
#     nowR = now[0]
#     nowC = now[1]

#     for i in range(1, 10):
#         board1[nowR][nowC] = i
#         if isValid(board1, now):
#             dfs(board1, stack)

# dfs(board, stack)

# for r in range(9):
#     for c in range(9):
#         print(results[0][r][c], end=" ")
#     print()

'''
# 사용해야 하는 알고리즘 = dfs, 백트래킹
    : dfs를 통해 현재 row의 queen 상태에 대해서 다음 row에 어디에 놓을 수 있는지 완전탐색
    : 백트래킹을 통해서 이미 아무곳도 놓을 수 없는 조합은 탐색 중단

# 문제 풀이 아이디어
    : 처음에 전혀 모르겠어서 블로그 찾아 보았다.
    : queen은 한 행에 1개만 놓을 수 있으므로 이차원 배열을 사용하지 않고 일반 배열 사용
    : 한 row 별로 1열 ~ n열까지 놓으면서 이전에 있는 queen들과 공존이 가능한지 확인
        : 어떤 열에도 놓을 수 없다면 그 상황에서는 탐색 중단

# 의사코드
    1. 입력을 받고 queen의 row별 위치를 기록할 [0] * n 배열을 선언한다.
    2. queen배열, row(현재 queen을 놓을 열), n을 인자로 받는 재귀함수를 만든다.
        2-1. 함수 내부에 cnt = 0을 선언한다.
        2-2. 현재 row == n이면 1을 리턴한다. (재귀함수 종료 조건)
        2-3. 현재 row의 열에 queen을 하나씩 놓아보면서
            2-3-1. 이미 놓인 queen과 세로, 대각선이 걸리지 않는지 확인한다.
            2-3-2. 걸려서 안되면 break
            2-3-3. 가능하다면 재귀함수에 인자를 현재까지 통과한 queen 배열, row + 1, n을 전달한다.
                : 이때 cnt += dfs()의 형태로 재귀함수의 결과가 cnt에 반영되도록 한다.
        2-4. 반복문을 빠져 나오면 cnt를 리턴한다.
            : 첫 함수에서는 답이 되는 cnt를 리턴하게 하고
            : 중간에 백트래킹 된 곳에서는 0을 리턴하게 하는 방치
'''
# n = int(input())
# queen = [0 for _ in range(n)]
# # queen 배열을 index가 행를 나타내고 value가 그 row의 열을 나타낸다.
#     # 한 row에는 1개의 queen 밖에 존재할 수 없기 때문에 가능한 방법

# # queen은 현재 row 이전까지 queen이 행별로 어느 열에 위치하는 지를 기록하고 있음.
#     # dfs로 실시해야 하는 이유는 bfs로 하면 queen의 위치가 꼬일 수 있기 때문에
# def dfs(queen, row, n):
#     # 💡 허용되는 case의 갯수를 저장하기 위한 변수
#     cnt = 0

#     # 마지막 row까지 통과하면 (row = n - 1까지) 1을 리턴한다 (cnt에 1개 추가)
#     if row == n:
#         return 1

#     # 현재 queen을 놓아야 하는 row에 모든 col을 놓아봄
#     for col in range(n):
#         queen[row] = col
#         # 그리고 나서 다른 row에 이미 놓인 queen들과 겹치는 곳은 없는지 확인
#         for i in range(row):
#             if queen[i] == col or abs(queen[i] - col) == row - i:
#                 break # 겹쳐서 안되면 break (백트래킹)
#         else:
#             cnt += dfs(queen, row + 1, n) # 모든 row와 비교가 통과하면 다음 row를 계산한다.

#     return cnt
#     # 첫 함수에서는 최종 cnt를 리턴하게 하고
#     # 중간에 백트래킹된 함수 (다음 row에 어떤 경우도 불가능한 경우)에는 0을 리턴하게 한다.



# print(dfs(queen, 0, n))

