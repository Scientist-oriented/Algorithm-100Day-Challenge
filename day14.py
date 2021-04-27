import sys
sys.stdin=open("input.txt", "r")

# 이취코 p.327 뱀 답코드
n = int(input())
k = int(input())
data = [[0] * (n + 1) for _ in range(n + 1)]
info = []

for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1

l = int(input())
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def simulate():
    x, y = 1, 1
    data[x][y] = 2
    direction = 0
    time = 0
    index = 0
    q = [(x, y)]
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]

        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2:
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                data[px][py] = 0
            if data[nx][ny] == 2:
                data[nx][ny] = 2
                q.append((nx, ny))
        else:
            time += 1
            break
    
        x, y = nx, ny
        time += 1
        if index < 1 and time == info[index][0]:
            direction = turn(direction, info[index][1])
            index += 1

    return time

print(simulate())

'''
# 이취코 p.327 뱀 내코드
from collections import deque

def rotate(direction):
    global heading
    if direction == "D":
        heading += 1
        if heading > 3:
            heading = 0
    elif direction == "L":
        heading -= 1
        if heading < 0:
            heading = 3

n = int(input())
k = int(input())
board = [[0] * n for _ in range(n)]

for _ in range(k):
    x, y = map(int, input().split())
    board[x - 1][y - 1] = 1

l = int(input())
moves = []

for _ in range(l):
    time, direction = map(str, input().split())
    moves.append((int(time), direction))

snake = deque()
snake.append((0, 0))
heading = 0
count = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for move in moves:
    time = move[0] - count
    direction = move[1]

    # 주어진 시간만큼 이동
    for _ in range(time):
        count += 1
        new_head = (snake[0][0] + dx[heading], snake[0][1] + dy[heading])
        
        # 벽에 부딪히거나 자기 몸에 부딪히면 게임 오버
        if new_head[0] < 0 or new_head[0] >= n or new_head[1] < 0 or new_head[1] >= n:
            print(count)
            exit()
        elif new_head in snake:
            print(count)
            exit()
        
        # 사과가 있으면 몸길이 늘어나고 없으면 꼬리 없애기
        if board[new_head[0]][new_head[1]] == 1:
            snake.appendleft(new_head)
        else:
            snake.appendleft(new_head)
            snake.pop()

    # 방향전환
    rotate(direction)

# 방향전환까지 다 했는데 안 끝났다면 마지막에 쭉 가다가 끝나는 점 잡기
while True:
    count += 1
    new_head = (snake[0][0] + dx[heading], snake[0][1] + dy[heading])

    # 벽에 부딪히거나 자기 몸에 부딪히면 게임 오버
    if new_head[0] < 0 or new_head[0] >= n or new_head[1] < 0 or new_head[1] >= n:
        print(count)
        exit()
    elif new_head in snake:
        print(count)
        exit()
    
    # 사과가 있으면 몸길이 늘어나고 없으면 꼬리 없애기
    if board[new_head[0]][new_head[1]] == 1:
        snake.appendleft(new_head)
    else:
        snake.appendleft(new_head)
        snake.pop()

# 이취코 p.325 자물쇠와 열쇠 답코드
def rotate(matrix):
    n = len(matrix) # 세로
    m = len(matrix[0]) # 가로
    new_matrix = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new_matrix[j][n - i - 1] = matrix[i][j]
    return new_matrix

def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)

    new_lock = [[0] * (n * 3) for _ in range(n * 3)]

    for i in range(n, n * 2):
        for j in range(n, n * 2):
            new_lock[i][j] = lock[i - n][j - n]

    for rotation in range(4):
        key = rotate(key)
        for x in range(n * 2):
            for y in range(n * 2):
                for i in range(m):
                    for j in range(m):
                        new_lock[i + x][j + y] += key[i][j]
        
                if check(new_lock):
                    return True
                else:
                    for i in range(m):
                        for j in range(m):
                            new_lock[i + x][j + y] -= key[i][j]

    return False


# 이취코 p.323 문자열 압축 다시풀어보기

def solution(s):
    result = len(s)
    for step in range(1, len(s) // 2 + 1):
        start = 0
        end = step
        count = 1
        compressed = ""
        while end <= len(s) - 1:
            if s[start:end] == s[start + step : end + step]:
                count += 1
            else:
                compressed += str(count) + s[start:end] if count > 1 else s[start:end] 
                count = 1
            start += step
            end += step
        compressed += str(count) + s[start:end + step] if count > 1 else s[start:end + step]
            
        result = min(result, len(compressed))
    
    return result
'''