import sys
sys.stdin=open("input.txt", "r")

# 구슬 탈출 2
N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
result = 11

for i in range(N):
    for j in range(M):
        if board[i][j] == "R":
            red = [i, j]
            board[i][j] = "."
        if board[i][j] == "B":
            blue = [i, j]
            board[i][j] = "."
        if board[i][j] == "O":
            target = [i, j]

def tiltUp(r, c):
    while True:
        r -= 1
        if board[r][c] == "O":
            return [r, c]
        if board[r][c] == "#":
            return [r + 1, c]

def tiltDown(r, c):
    while True:
        r += 1
        if board[r][c] == "O":
            return [r, c]
        if board[r][c] == "#":
            return [r - 1, c]

def tiltLeft(r, c):
    while True:
        c -= 1
        if board[r][c] == "O":
            return [r, c]
        if board[r][c] == "#":
            return [r, c + 1]

def tiltRight(r, c):
    while True:
        c += 1
        if board[r][c] == "O":
            return [r, c]
        if board[r][c] == "#":
            return [r, c - 1]

def dfs(red, blue, numOfTries):
    #print(red, blue, numOfTries)
    if numOfTries > 10:
        return

    global result
    if red == target:
        #print(f"ans{numOfTries}", red, blue, numOfTries)
        result = min(result, numOfTries)
        return

    nextRed = tiltUp(red[0], red[1])
    nextBlue = tiltUp(blue[0], blue[1])
    if nextBlue != target:
        if nextRed == nextBlue:
            if red[0] < blue[0]:
                nextBlue[0] += 1
            else:
                nextRed[0] += 1
        if not visited[nextRed[0]][nextRed[1]]:
            visited[nextRed[0]][nextRed[1]] = True
            #print("UP")
            dfs(nextRed, nextBlue, numOfTries + 1)
            visited[nextRed[0]][nextRed[1]] = False

    nextRed = tiltDown(red[0], red[1])
    nextBlue = tiltDown(blue[0], blue[1])
    if nextBlue != target:
        if nextRed == nextBlue:
            if red[0] > blue[0]:
                nextBlue[0] -= 1
            else:
                nextRed[0] -= 1
        if not visited[nextRed[0]][nextRed[1]]:
            visited[nextRed[0]][nextRed[1]] = True
            #print("Down")
            dfs(nextRed, nextBlue, numOfTries + 1)
            visited[nextRed[0]][nextRed[1]] = False

    nextRed = tiltLeft(red[0], red[1])
    nextBlue = tiltLeft(blue[0], blue[1])
    if nextBlue != target:
        if nextRed == nextBlue:
            if red[1] < blue[1]:
                nextBlue[1] += 1
            else:
                nextRed[1] += 1
        if not visited[nextRed[0]][nextRed[1]]:
            visited[nextRed[0]][nextRed[1]] = True
            #print("Left")
            dfs(nextRed, nextBlue, numOfTries + 1)
            visited[nextRed[0]][nextRed[1]] = False

    nextRed = tiltRight(red[0], red[1])
    nextBlue = tiltRight(blue[0], blue[1])
    if nextBlue != target:
        if nextRed == nextBlue:
            if red[1] > blue[1]:
                nextBlue[1] -= 1
            else:
                nextRed[1] -= 1
        if not visited[nextRed[0]][nextRed[1]]:
            visited[nextRed[0]][nextRed[1]] = True
            #print("Right")
            dfs(nextRed, nextBlue, numOfTries + 1)
            visited[nextRed[0]][nextRed[1]] = False

visited[red[0]][red[1]] = True
dfs(red, blue, 0)
print(result if result < 11 else -1)