import sys
sys.stdin=open("input.txt", "r")

# 감시
def printPretty():
    for i in range(N):
        print(board[i])
    print()

def seeLeft(r, c):
    nc = c - 1
    while True:
        if nc < 0 or board[r][nc] == 6:
            return
        if board[r][nc] > 0:
            nc -= 1
        else:
            board[r][nc] -= 1
            nc -= 1

def cancelLeft(r, c):
    nc = c - 1
    while True:
        if nc < 0 or board[r][nc] == 6:
            return
        if board[r][nc] > 0:
            nc -= 1
        else:
            board[r][nc] += 1
            nc -= 1

def seeRight(r, c):
    nc = c + 1
    while True:
        if nc > M - 1 or board[r][nc] == 6:
            return
        if board[r][nc] > 0:
            nc += 1
        else:
            board[r][nc] -= 1
            nc += 1

def cancelRight(r, c):
    nc = c + 1
    while True:
        if nc > M - 1 or board[r][nc] == 6:
            return
        if board[r][nc] > 0:
            nc += 1
        else:
            board[r][nc] += 1
            nc += 1

def seeUp(r, c):
    nr = r - 1
    while True:
        if nr < 0 or board[nr][c] == 6:
            return
        if board[nr][c] > 0:
            nr -= 1
        else:
            board[nr][c] -= 1
            nr -= 1

def cancelUp(r, c):
    nr = r - 1
    while True:
        if nr < 0 or board[nr][c] == 6:
            return
        if board[nr][c] > 0:
            nr -= 1
        else:
            board[nr][c] += 1
            nr -= 1

def seeDown(r, c):
    nr = r + 1
    while True:
        if nr > N - 1 or board[nr][c] == 6:
            return
        if board[nr][c] > 0:
            nr += 1
        else:
            board[nr][c] -= 1
            nr += 1

def cancelDown(r, c):
    nr = r + 1
    while True:
        if nr > N - 1 or board[nr][c] == 6:
            return
        if board[nr][c] > 0:
            nr += 1
        else:
            board[nr][c] += 1
            nr += 1

def cameraOn(r, c, num, type):
    if num == 1:
        if type == 1:
            seeRight(r, c)
        elif type == 2:
            seeDown(r, c)
        elif type == 3:
            seeLeft(r, c)
        else:
            seeUp(r, c)
    elif num == 2:
        if type == 1:
            seeLeft(r, c)
            seeRight(r, c)
        else:
            seeUp(r, c)
            seeDown(r, c)
    elif num == 3:
        if type == 1:
            seeUp(r, c)
            seeRight(r, c)
        elif type == 2:
            seeRight(r, c)
            seeDown(r, c)
        elif type == 3:
            seeDown(r, c)
            seeLeft(r, c)
        else:
            seeLeft(r, c)
            seeUp(r, c)
    elif num == 4:
        if type == 1:
            seeLeft(r, c)
            seeUp(r, c)
            seeRight(r, c)
        elif type == 2:
            seeUp(r, c)
            seeRight(r, c)
            seeDown(r, c)
        elif type == 3:
            seeUp(r, c)
            seeDown(r, c)
            seeLeft(r, c)
        else:
            seeRight(r, c)
            seeDown(r, c)
            seeLeft(r, c)
    elif num == 5:
        seeUp(r, c)
        seeDown(r, c)
        seeLeft(r, c)
        seeRight(r, c)

def cameraOff(r, c, num, type):
    if num == 1:
        if type == 1:
            cancelRight(r, c)
        elif type == 2:
            cancelDown(r, c)
        elif type == 3:
            cancelLeft(r, c)
        else:
            cancelUp(r, c)
    elif num == 2:
        if type == 1:
            cancelLeft(r, c)
            cancelRight(r, c)
        else:
            cancelUp(r, c)
            cancelDown(r, c)
    elif num == 3:
        if type == 1:
            cancelUp(r, c)
            cancelRight(r, c)
        elif type == 2:
            cancelRight(r, c)
            cancelDown(r, c)
        elif type == 3:
            cancelDown(r, c)
            cancelLeft(r, c)
        else:
            cancelLeft(r, c)
            cancelUp(r, c)
    elif num == 4:
        if type == 1:
            cancelLeft(r, c)
            cancelUp(r, c)
            cancelRight(r, c)
        elif type == 2:
            cancelUp(r, c)
            cancelRight(r, c)
            cancelDown(r, c)
        elif type == 3:
            cancelUp(r, c)
            cancelDown(r, c)
            cancelLeft(r, c)
        else:
            cancelRight(r, c)
            cancelDown(r, c)
            cancelLeft(r, c)
    elif num == 5:
        cancelUp(r, c)
        cancelDown(r, c)
        cancelLeft(r, c)
        cancelRight(r, c)

def getNextCoord(r, c):
    if c < M - 1:
        return (r, c + 1)
    else:
        return (r + 1, 0)

def getUnwatchedArea():
    result = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                result += 1
    return result

def dfs(r, c):
    global result

    if r == N:
        result = min(result, getUnwatchedArea())
        return

    nr, nc = getNextCoord(r, c)

    if board[r][c] <= 0 or board[r][c] > 5:
        dfs(nr, nc)
    else:
        if board[r][c] == 1:
            cameraOn(r, c, 1, 1)
            dfs(nr, nc)
            cameraOff(r, c, 1, 1)

            cameraOn(r, c, 1, 2)
            dfs(nr, nc)
            cameraOff(r, c, 1, 2)

            cameraOn(r, c, 1, 3)
            dfs(nr, nc)
            cameraOff(r, c, 1, 3)

            cameraOn(r, c, 1, 4)
            dfs(nr, nc)
            cameraOff(r, c, 1, 4)
        elif board[r][c] == 2:
            cameraOn(r, c, 2, 1)
            dfs(nr, nc)
            cameraOff(r, c, 2, 1)

            cameraOn(r, c, 2, 2)
            dfs(nr, nc)
            cameraOff(r, c, 2, 2)

        elif board[r][c] == 3:
            cameraOn(r, c, 3, 1)
            dfs(nr, nc)
            cameraOff(r, c, 3, 1)

            cameraOn(r, c, 3, 2)
            dfs(nr, nc)
            cameraOff(r, c, 3, 2)

            cameraOn(r, c, 3, 3)
            dfs(nr, nc)
            cameraOff(r, c, 3, 3)

            cameraOn(r, c, 3, 4)
            dfs(nr, nc)
            cameraOff(r, c, 3, 4)
        
        elif board[r][c] == 4:
            cameraOn(r, c, 4, 1)
            dfs(nr, nc)
            cameraOff(r, c, 4, 1)

            cameraOn(r, c, 4, 2)
            dfs(nr, nc)
            cameraOff(r, c, 4, 2)

            cameraOn(r, c, 4, 3)
            dfs(nr, nc)
            cameraOff(r, c, 4, 3)

            cameraOn(r, c, 4, 4)
            dfs(nr, nc)
            cameraOff(r, c, 4, 4)
        
        elif board[r][c] == 5:
            cameraOn(r, c, 5, 1)
            dfs(nr, nc)
            cameraOff(r, c, 5, 1)
    
N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

result = 100
dfs(0, 0)

print(result)

'''
# 경사로
N, L = map(int, input().split())
board = list()
for _ in range(N):
    board.append(list(map(int, input().split())))

def getVerticals(board):
    transposedBoard = list(map(list, zip(*board)))
    return transposedBoard

def isDownPossible(road, checks, start):
    if start + L > N - 1:
        return False
    height = road[start]
    for i in range(1, L + 1):
        if road[start + i] != height - 1 or checks[start + i] == True:
            return False
    return True

def isUpPossible(road, checks, start):
    if start - L < 0:
        return False
    height = road[start]
    for i in range(1, L + 1):
        if road[start - i] !=  height - 1 or checks[start - i] == True:
            return False
    return True

def buildDown(checks, start):
    for i in range(1, L + 1):
        checks[start + i] = True
    return checks

def buildUp(checks, start):
    for i in range(1, L + 1):
        checks[start - i] = True
    return checks

def isCrossPossible(road):
    i = 0
    checks = [False] * N
    while i < N - 1:
        if road[i] == road[i + 1]:
            i += 1
        else:
            if road[i] > road[i + 1]:
                if isDownPossible(road, checks, i):
                    checks = buildDown(checks, i)
                    i += L
                else:
                    return False
            else:
                if isUpPossible(road, checks, i + 1):
                    checks = buildUp(checks, i + 1)
                    i += 1
                else:
                    return False
    return True

result = 0
for road in board:
    if isCrossPossible(road):
        result += 1

for road in getVerticals(board):
    if isCrossPossible(road):
        result += 1

print(result)


# 로봇 청소기

def printPretty():
    for i in range(N):
        print(board[i])

def turnLeft(cleaner):
    r, c, d = cleaner
    return (r, c, d - 1) if d != 0 else (r, c, 3)

def searchLeft(cleaner):
    r, c, d = cleaner
    if d == 0:
        if board[r][c - 1] == 0:
            return True
        else:
            return False
    elif d == 1:
        if board[r - 1][c] == 0:
            return True
        else:
            return False
    elif d == 2:
        if board[r][c + 1] == 0:
            return True
        else:
            return False
    else:
        if board[r + 1][c] == 0:
            return True
        else:
            return False

def moveLeftAndClean(cleaner):
    global result
    cleaner = turnLeft(cleaner)
    r, c, d = cleaner
    if d == 0:
        result += 1
        board[r - 1][c] = 2
        return (r - 1, c, d)
    elif d == 1:
        result += 1
        board[r][c + 1] = 2
        return (r, c + 1, d)
    elif d == 2:
        result += 1
        board[r + 1][c] = 2
        return (r + 1, c, d)
    else:
        result += 1
        board[r][c - 1] = 2
        return (r, c - 1, d)

def moveBack(cleaner):
    r, c, d = cleaner
    if d == 0 and board[r + 1][c] != 1:
        return (r + 1, c, d)
    elif d == 1 and board[r][c - 1] != 1:
        return (r, c - 1, d)
    elif d == 2 and board[r - 1][c] != 1:
        return (r - 1, c, d)
    elif d == 3 and board[r][c + 1] != 1:
        return (r, c + 1, d)
    else:
        return False

N, M = map(int, input().split())
r, c, d = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
result = 1
board[r][c] = 2
cleaner = (r, c, d)
    
while True:
    for _ in range(4):
        if not searchLeft(cleaner):
            cleaner = turnLeft(cleaner)
        else:
            cleaner = moveLeftAndClean(cleaner)
            break
    else:
        cleaner = moveBack(cleaner)
    if not cleaner:
        break
print(result)

# 테트로미노
def getBlueBlocks(r, c):
    blocks = []
    if c + 3 < M:
        blocks.append([(r, c), (r, c + 1), (r, c + 2), (r, c + 3)])
    if r + 3 < N:
        blocks.append([(r, c), (r + 1, c), (r + 2, c), (r + 3, c)])
    return blocks

def getYellowBlocks(r, c):
    blocks = []
    if r + 1 < N and c + 1 < M:
        blocks.append([(r, c), (r + 1, c), (r, c + 1), (r + 1, c + 1)])
    return blocks

def getOrangeBlocks(r, c):
    blocks = []
    if r + 2 < N and c + 1 < M:
        blocks.extend([
            [(r, c), (r + 1, c), (r + 2, c), (r + 2, c + 1)],
            [(r, c + 1), (r + 1, c + 1), (r + 2, c + 1), (r + 2, c)],
            [(r, c), (r, c + 1), (r + 1, c + 1), (r + 2, c + 1)],
            [(r, c), (r + 1, c), (r + 2, c), (r, c + 1)],
        ])
    if r + 1 < N and c + 2 < M:
        blocks.extend([
            [(r, c), (r + 1, c), (r, c + 1), (r, c + 2)],
            [(r, c), (r, c + 1), (r, c + 2), (r + 1, c + 2)],
            [(r + 1, c), (r + 1, c + 1), (r + 1, c + 2), (r, c + 2)],
            [(r, c), (r + 1, c), (r + 1, c + 1), (r + 1, c + 2)],
        ])
    return blocks

def getGreenBlocks(r, c):
    blocks = []
    if r + 2 < N and c + 1 < M:
        blocks.extend([
            [(r, c), (r + 1, c), (r + 1, c + 1), (r + 2, c + 1)],
            [(r, c + 1), (r + 1, c + 1), (r + 1, c), (r + 2, c)],
        ])
    if r + 1 < N and c + 2 < M:
        blocks.extend([
            [(r + 1, c), (r + 1, c + 1), (r, c + 1), (r, c + 2)],
            [(r, c), (r, c + 1), (r + 1, c + 1), (r + 1, c + 2)],
        ])
    return blocks

def getPurpleBlocks(r, c):
    blocks = []
    if r + 1 < N and c + 2 < M:
        blocks.extend([
            [(r, c), (r, c + 1), (r, c + 2), (r + 1, c + 1)],
            [(r, c + 1), (r + 1, c), (r + 1, c + 1), (r + 1, c + 2)],
        ])
    if r + 2 < N and c + 1 < M:
        blocks.extend([
            [(r, c + 1), (r + 1, c), (r + 1, c + 1), (r + 2, c + 1)],
            [(r, c), (r + 1, c), (r + 2, c), (r + 1, c + 1)],
        ])
    return blocks

def getAllBlocks(r, c):
    blocks = []
    blocks.extend(getBlueBlocks(r, c))
    blocks.extend(getYellowBlocks(r, c))
    blocks.extend(getOrangeBlocks(r, c))
    blocks.extend(getGreenBlocks(r, c))
    blocks.extend(getPurpleBlocks(r, c))
    return blocks

def getHighestBlock(blocks):
    maximum = 0
    for block in blocks:
        result = 0
        for piece in block:
            result += board[piece[0]][piece[1]]
        maximum = max(result, maximum)
    return maximum


N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

result = 0
for r in range(N):
    for c in range(M):
        blocks = getAllBlocks(r, c)
        result = max(result, getHighestBlock(blocks))
print(result)




# 주사위 굴리기

# 순서대로 밑, 앞, 뒤, 왼쪽, 오른쪽, 위
dice = [0, 0, 0, 0, 0, 0]

# 움직이면 인덱스가 어떻게 바뀌는가?
    # 순서대로 동서북남
roll = {
    1: [4, 1, 2, 0, 5, 3],
    2: [3, 1, 2, 5, 0, 4],
    3: [2, 0, 5, 3, 4, 1],
    4: [1, 5, 0, 3, 4, 2],
}

def rollDice(dice, command):
    newDice = [0] * 6
    for i in range(6):
        newDice[i] = dice[roll[command][i]]
    return newDice

def moveDice(dicePos, command):
    if command == 1 and dicePos[1] + 1 <= M - 1:
        return (dicePos[0], dicePos[1] + 1)
    elif command == 2 and dicePos[1] - 1 >= 0:
        return (dicePos[0], dicePos[1] - 1)
    elif command == 3 and dicePos[0] - 1 >= 0:
        return (dicePos[0] - 1, dicePos[1])
    elif command == 4 and dicePos[0] + 1 <= N - 1:
        return (dicePos[0] + 1, dicePos[1])
    else:
        return False
        

N, M, x, y, K = map(int, input().split())
board = [[0 for _ in range(M)] for _ in range(N)]
dicePos = (x, y)
for i in range(N):
    nums = list(map(int, input().split()))
    for j in range(M):
        board[i][j] = nums[j]
commands = list(map(int, input().split()))

for command in commands:
    newDicePos = moveDice(dicePos, command)
    if not newDicePos:
        continue
    dicePos = newDicePos
    dice = rollDice(dice, command)
    if board[dicePos[0]][dicePos[1]] == 0:
        board[dicePos[0]][dicePos[1]] = dice[0]
    else:
        dice[0] = board[dicePos[0]][dicePos[1]]
        board[dicePos[0]][dicePos[1]] = 0
    print(dice[5])


    
    


# 낚시왕
R, C, M = map(int, input().split())
board = [[[] for _ in range(C)] for _ in range(R)]

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    board[r - 1][c - 1].append((s, d, z))

def printPretty(board):
    for r in range(R):
        print(board[r])

def getSharkPosition(r, c, s, d):
    if d == 1:
        s %=  (2 * (R - 1))
        if r - s >= 0:
            return (r - s, c, 1)
        else:
            if s - r <= R - 1:
                return (s - r, c, 2)
            else:
                rPos = 2 * (R - 1) - (s - r)
                return (rPos, c, 1)
    elif d == 2:
        s %= (2 * (R - 1))
        if r + s <= R - 1:
            return (r + s, c, 2)
        else:
            rPos = 2 * (R - 1) - (r + s)
            if rPos >= 0:
                return (rPos, c, 1)
            else:
                return (-rPos, c, 2)
    elif d == 3:
        s %= (2 * (C - 1))
        if c + s <= C - 1:
            return (r, c + s, 3)
        else:
            cPos = 2 * (C - 1) - (c + s)
            if cPos >= 0:
                return (r, cPos, 4)
            else:
                return (r, -cPos, 3)
    else:
        s %= (2 * (C - 1))
        if c - s >= 0:
            return (r, c - s, 4)
        else:
            if s - c <= C  - 1:
                return (r, s - c, 3)
            else:
                cPos = 2 * (C - 1) - (s - c)
                return (r, cPos, 4)

def eatShark(board):
    for r in range(R):
        for c in range(C):
            if len(board[r][c]) > 1:
                board[r][c].sort(key=lambda x: x[2])
                board[r][c] = [board[r][c][-1]]
    return board

def moveShark(board):
    newBoard = [[[] for _ in range(C)] for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if board[r][c]:
                s, d, z = board[r][c].pop()
                nr, nc, nd = getSharkPosition(r, c, s, d)
                newBoard[nr][nc].append((s, nd, z))
    return newBoard

def catchShark(board, time):
    global result
    col = time - 1
    for r in range(R):
        if board[r][col]:
            result += board[r][col][0][2]
            board[r][col] = []
            return board
    return board

time = 0
result = 0

while time <= C - 1:
    time += 1
    board = catchShark(board, time)
    board = moveShark(board)
    board = eatShark(board)
    # printPretty(board)
    # print()

print(result)



# 뱀
from collections import deque

N = int(input())
K = int(input())
board = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    board[r - 1][c - 1] = 2

L = int(input())
moves = deque()
for _ in range(L):
    time, dir = input().split()
    moves.append((int(time), dir))

snake = deque()
snake.append((0, 0))

# 오른쪽 0
# 위쪽 1
# 왼쪽 2
# 아래쪽 3

def changeDirection(now, turn):
    if turn == "L":
        return now + 1 if now != 3 else 0
    else:
        return now - 1 if now != 0 else 3

def go(direction):
    headR, headC = snake[-1]
    if direction == 0:
        if headC + 1 < N and (headR, headC + 1) not in snake:
            snake.append((headR, headC + 1))
            if board[headR][headC + 1] == 2:
                board[headR][headC + 1] = 0
                return True
            else:
                snake.popleft()
                return True
        else:
            return False
    elif direction == 1:
        if headR - 1 > -1 and (headR - 1, headC) not in snake:
            snake.append((headR - 1, headC))
            if board[headR - 1][headC] == 2:
                board[headR - 1][headC] = 0
                return True
            else:
                snake.popleft()
                return True
        else:
            return False
    elif direction == 2:
        if headC - 1 > -1 and not (headR, headC - 1) in snake:
            snake.append((headR, headC - 1))
            if board[headR][headC - 1] == 2:
                board[headR][headC - 1] = 0
                return True
            else:
                snake.popleft()
                return True
        else:
            return False
    else:
        if headR + 1 < N and not (headR + 1, headC) in snake:
            snake.append((headR + 1, headC))
            if board[headR + 1][headC] == 2:
                board[headR + 1][headC] = 0
                return True
            else:
                snake.popleft()
                return True
        else:
            return False

def isPossible():
    headR, headC = snake.pop()
    if (headR, headC) in snake:
        return False
    elif headR < 0 or headR > N - 1:
        return False
    elif headC < 0 or headC > N - 1:
        return False
    else:
        snake.append((headR, headC))
        return True

def play():
    direction = 0
    toGo = 0
    total = 0
    while moves:
        move = moves.popleft()
        toGo = move[0] - total
        while toGo > 0:
            # print(total, direction, snake)
            if go(direction):
                toGo -= 1
                total += 1
            else:
                return total + 1
        direction = changeDirection(direction, move[1])
    while True:
        # print(total, direction, snake)
        if go(direction):
            total += 1
        else:
            return total + 1

print(play())
'''