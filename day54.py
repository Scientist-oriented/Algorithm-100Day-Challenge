import sys
sys.stdin=open("input.txt", "r")

# 2048 (Easy)

import copy

def printPretty(board):
    for i in range(N):
        print(board[i])

def moveUp(board):
    newboard = copy.deepcopy(board)
    for r in range(1, N):
        for c in range(N):
            nowR = r
            if newboard[r][c] != 0:
                nextR = nowR - 1
                while nextR >= 0:
                    if newboard[nextR][c] == 0:
                        newboard[nextR][c] = newboard[nowR][c]
                        newboard[nowR][c] = 0
                        nowR = nextR
                        nextR -= 1
                    else:
                        break
    return newboard

def mergeUp(board):
    newboard = copy.deepcopy(board)
    for r in range(N - 1):
        for c in range(N):
            if newboard[r][c] == newboard[r + 1][c]:
                newboard[r][c] *= 2
                newboard[r + 1][c] = 0
    return newboard

def moveDown(board):
    newboard = copy.deepcopy(board)
    for r in range(N - 2, -1, -1):
        for c in range(N):
            nowR = r # 여기서 그냥 r을 그대로 쓰면 c를 돌리는 for문에 영향을 받는다!
            if newboard[nowR][c] != 0:
                nextR = nowR + 1
                while nextR <= N - 1:
                    if newboard[nextR][c] == 0:
                        newboard[nextR][c] = newboard[nowR][c]
                        newboard[nowR][c] = 0
                        nowR = nextR
                        nextR += 1
                    else:
                        break
    return newboard

def mergeDown(board):
    newboard = copy.deepcopy(board)
    for r in range(N - 1, 0, -1):
        for c in range(N):
            if newboard[r][c] == newboard[r - 1][c]:
                newboard[r][c] *= 2
                newboard[r - 1][c] = 0
    return newboard

def moveLeft(board):
    newboard = copy.deepcopy(board)
    for c in range(1, N):
        for r in range(N):
            nowC = c
            if newboard[r][nowC] != 0:
                nextC = nowC - 1
                while nextC >= 0:
                    if newboard[r][nextC] == 0:
                        newboard[r][nextC] = newboard[r][nowC]
                        newboard[r][nowC] = 0
                        nowC = nextC
                        nextC -= 1
                    else:
                        break
    return newboard
                    
def mergeLeft(board):
    newboard = copy.deepcopy(board)
    for c in range(N - 1):
        for r in range(N):
            if newboard[r][c] == newboard[r][c + 1]:
                newboard[r][c] *= 2
                newboard[r][c + 1] = 0
    return newboard

def moveRight(board):
    newboard = copy.deepcopy(board)
    for c in range(N - 2, -1, -1):
        for r in range(N):
            nowC = c
            if newboard[r][nowC] != 0:
                nextC = nowC + 1
                while nextC <= N - 1:
                    if newboard[r][nextC] == 0:
                        newboard[r][nextC] = newboard[r][nowC]
                        newboard[r][nowC] = 0
                        nowC = nextC
                        nextC += 1
                    else:
                        break
    return newboard

def mergeRight(board):
    newboard = copy.deepcopy(board)
    for c in range(N - 1, 0, -1):
        for r in range(N):
            if newboard[r][c] == newboard[r][c - 1]:
                newboard[r][c] *= 2
                newboard[r][c - 1] = 0
    return newboard

def getHighestOnBoard(board):
    result = 0
    for r in range(N):
        for c in range(N):
            result = max(board[r][c], result)
    return result

def up(board):
    return moveUp(mergeUp(moveUp(board)))

def down(board):
    return moveDown(mergeDown(moveDown(board)))

def left(board):
    return moveLeft(mergeLeft(moveLeft(board)))

def right(board):
    return moveRight(mergeRight(moveRight(board)))

def dfs(board, tries):
    global ans

    if tries > 5:
        return

    upBoard = up(board)
    ans = max(getHighestOnBoard(upBoard), ans)
    dfs(upBoard, tries + 1)

    downBoard = down(board)
    ans = max(getHighestOnBoard(downBoard), ans)
    dfs(downBoard, tries + 1)

    leftBoard = left(board)
    ans = max(getHighestOnBoard(leftBoard), ans)
    dfs(leftBoard, tries + 1)

    rightBoard = right(board)
    ans = max(getHighestOnBoard(rightBoard), ans)
    dfs(rightBoard, tries + 1)

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
ans = 0
dfs(board, 1)
print(ans)

# N = 7
# board = [
#     [2, 2, 2, 2, 2, 2, 2],
#     [2, 0, 2, 2, 2, 2, 2],
#     [2, 0, 2, 2, 2, 2, 2],
#     [2, 0, 2, 2, 2, 2, 2],
#     [2, 2, 2, 0, 2, 2, 2],
#     [2, 2, 2, 2, 2, 2, 0],
#     [2, 2, 2, 2, 2, 2, 0],
# ]

# printPretty(right(right(right(board))))
                 