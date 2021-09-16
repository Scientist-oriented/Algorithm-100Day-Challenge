import sys
sys.stdin=open("input.txt", "r")

# 색종이 붙이기
import sys
sys.setrecursionlimit(10**8)
board = [list(map(int, input().split())) for _ in range(10)]
papers = [0 for _ in range(6)]
result = 26

def isPossible(r, c, size):
    if r + size - 1 > 9 or c + size - 1 > 9:
        return False
    for i in range(r, r + size):
        for j in range(c, c + size):
            if board[i][j] != 1:
                return False
    return True

def toggle(r, c, size):
    for i in range(r, r + size):
        for j in range(c, c + size):
            board[i][j] = 1 - board[i][j]

def isAllCovered():
    for i in range(10):
        for j in range(10):
            if board[i][j] != 0:
                return False
    return True

def nextRC(r, c):
    if c + 1 > 9:
        return (r + 1, 0)
    else:
        return (r, c + 1)

def printBoard():
    for l in board:
        print(l)

def isPossiblePapers():
    for i in range(1, 6):
        if papers[i] > 5:
            return False
    return True

def dfs(r, c):
    global result
    if r == 9 and c == 9:
        if board[r][c] == 0:
            if isAllCovered() and isPossiblePapers():
                result = min(sum(papers), result)
            return
        else:
            toggle(r, c, 1)
            papers[1] += 1
            if isAllCovered() and isPossiblePapers():
                result = min(sum(papers), result)
            toggle(r, c, 1)
            papers[1] -= 1
            return


    if not isPossiblePapers():
        return
    
    if board[r][c] == 1:
        for size in range(1, 6):
            if isPossible(r, c, size):
                nr, nc = nextRC(r, c)
                toggle(r, c, size)
                papers[size] += 1
                dfs(nr, nc)
                toggle(r, c, size)
                papers[size] -= 1
    else:
        nr, nc = nextRC(r, c)
        dfs(nr, nc)
                
dfs(0, 0)
print(result if result < 26 else -1)



'''
# 파이프 옮기기
import sys
sys.setrecursionlimit(10**9)
'''
'''
가로: 0
대각선: 1
세로: 2
'''
'''
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
result = 0

def isPossible(r, c, nextPos):
    if nextPos == 0:
        if c + 1 < N and board[r][c + 1] != 1:
            return True
        else:
            return False
    elif nextPos == 1:
        if r + 1 < N and c + 1 < N and board[r][c + 1] != 1 and board[r + 1][c] != 1 and board[r + 1][c + 1] != 1:
            return True
        else:
            return False
    else:
        if r + 1 < N and board[r + 1][c] != 1:
            return True
        else:
            return False

def dfs(r, c, pos):
    global result
    if r == N - 1 and c == N - 1:
        result += 1
        return
    if pos == 0 or pos == 1:
        if isPossible(r, c, 0):
            dfs(r, c + 1, 0)
    
    if pos == 0 or pos == 1 or pos == 2:
        if isPossible(r, c, 1):
            dfs(r + 1, c + 1, 1)
    
    if pos == 1 or pos == 2:
        if isPossible(r, c, 2):
            dfs(r + 1, c, 2)

dfs(0, 1, 0)
print(result)


# 게리맨더링
from itertools import combinations

N = int(input())
nodes = [i for i in range(N)]
peo = list(map(int, input().split()))
vertice = []
for _ in range(N):
    connection = list(map(int, input().split()))
    connection.pop(0)
    vertice.append(connection)

# dfs를 통해서 해당 도시들이 다 연결되어 있는지 확인
def isConnected(nodes):
    visited = [False] * N
    stack = []
    stack.append(nodes[0])
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            for next in vertice[node]:
                if next - 1 in nodes: # 같은 선거구를 통해 연결된 길만!
                    stack.append(next - 1)
    for node in nodes:
        if not visited[node]:
            return False
    return True

def numOfPeo(nodes):
    result = 0
    for node in nodes:
        result += peo[node]
    return result

result = 1000

for i in range(1, N // 2 + 1):
    for combi in combinations(nodes, i):
        red = list(combi)
        blue = list(filter(lambda x: x not in red, nodes))
        if isConnected(red) and isConnected(blue):
            #print(f"red: {red} blue: {blue} numOfPeo(red): {numOfPeo(red)} numOfPeo(blue): {numOfPeo(blue)}")
            result = min(result, abs(numOfPeo(red) - numOfPeo(blue)))

print(result if result != 1000 else -1)
'''

    
